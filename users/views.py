from urllib import request
from urllib.request import Request
from django.shortcuts import redirect, render
import mysql.connector as sql
import environ
from django.core.mail import send_mail
import math, random
from setuptools import Require

env = environ.Env()
environ.Env.read_env()
n = ''
ph = ''
em = ''
pwd = ''
ot = ''
sus = ''
ddate = ''
time = ''
datetime = ''
#datetime = '2021-12-31 15:40:10'
dvacina = ''

def error(request):
    return render(request, 'users/error.html')

def vacMain(request):
    m=sql.connect(host= env('DATABASE_HOST'),user= env('DATABASE_USER'),passwd= env('DATABASE_PASS'),database= env('DATABASE_NAME'))
    cursor=m.cursor()
    c="SELECT * FROM doses;"
    cursor.execute(c)
    tablee=cursor.fetchall()

    return render(request, 'users/vacinas.html',{'tablee':tablee})

def generateOTP():
     digits = '0123456789'
     OTP = ''
     for i in range(4) :
         OTP += digits[math.floor(random.random() * 10)]
     return OTP

def send_otp():
    global ot
    ot=generateOTP()
    send_mail(
        'Verificação Imuniza',
        'Seu código é {}'.format(ot),
        'probit454@gmail.com',
        ['{}'.format(em)],
        fail_silently=False,
     )

def register(request):
    global n,ph,em,pwd
    if request.method == 'POST':
        m=sql.connect(host= env('DATABASE_HOST'),user= env('DATABASE_USER'),passwd= env('DATABASE_PASS'),database= env('DATABASE_NAME'))
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
             if key=='name':
                 n=value
             if key=='phone':
                 ph=value
             if key=='mail':
                 em=value
             if key=='password':
                 pwd=value
             
        c="INSERT INTO users (name,phone_number,email,password) VALUES('{}','{}','{}','{}');".format(n,ph,em,pwd)
        cursor.execute(c)
        m.commit()
        return redirect('login')

    return render(request, 'users/register.html') 


def login(request):
    global em,pwd
    if request.method == 'POST':
        m=sql.connect(host= env('DATABASE_HOST'),user= env('DATABASE_USER'),passwd= env('DATABASE_PASS'),database= env('DATABASE_NAME'))
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
             if key=='mail':
                 em=value
             if key=='password':
                 pwd=value
             
        c="SELECT * FROM users WHERE email='{}' and password='{}';".format(em,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return redirect('error')
        else:
            send_otp()
            return redirect('verification')     
    return render(request, 'users/login.html')


def verification(request):
    if request.method == 'POST':
        otp = request.POST.get('otpp')
        if otp == ot:
            return redirect('vacinas')
        else:
            print(ot)

    return render(request, 'users/otp.html')

def appointment(request):
    global em,n,ph,dvacina,sus,ddate,time,datetime
    if request.method == 'POST':
        m=sql.connect(host= env('DATABASE_HOST'),user= env('DATABASE_USER'),passwd= env('DATABASE_PASS'),database= env('DATABASE_NAME'))
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
             if key=='dvacina':
                 dvacina=value
             if key=='sus':
                 sus=value
             if key=='ddata':
                 ddate=value
             if key=='hora':
                 time=value
        datetime = str(ddate)+' '+str(time)
        c="INSERT INTO vaccination (name,phone_number,email,dvaccine,sus,datetime) VALUES('{}','{}','{}','{}','{}','{}');".format(n,ph,em,dvacina,sus,datetime)
        cursor.execute(c)
        m.commit()
        return redirect('vacinas')
    return render(request, 'users/schedule.html')


