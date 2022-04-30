let btnAdd = document.querySelector('button');
let table = document.querySelector('table');


let nomeInput = document.querySelector('#nome');
let horaInput = document.querySelector('#hora');
let dataInput = document.querySelector('#data');


btnAdd.addEventListener('click', () => {
    let nome = nomeInput.value;
    let hora = horaInput.value;
    let data = dataInput.value;

    let template = `
                <tr>
                    <td>${nome}</td>
                    <td>${hora}</td>
                    <td>${data}</td>
                </tr>`;

    table.innerHTML += template;
});