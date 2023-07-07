
document.addEventListener('DOMContentLoaded', function() {
  const url = 'https://mindicador.cl/api';
  const options = {
    method: 'GET',
  };

  fetch(url, options)
    .then(response => response.json())
    .then(data => {
      const currencyContainer = document.getElementById('currency-container');
      const currencies = ['dolar', 'euro', 'uf', 'utm'];

      currencies.forEach(currency => {
        const indicator = data[currency];
        const currencyDiv = document.createElement('div');
        currencyDiv.classList.add('currency');

        const nameElement = document.createElement('span');
        nameElement.innerText = indicator.nombre;

        const valueElement = document.createElement('span');
        valueElement.innerText = `Valor: ${indicator.valor}`;

        const unitElement = document.createElement('span');
        unitElement.innerText = `Unidad: ${indicator.unidad_medida}`;

        currencyDiv.appendChild(nameElement);
        currencyDiv.appendChild(valueElement);
        currencyDiv.appendChild(unitElement);

        currencyContainer.appendChild(currencyDiv);
      });
    })
    .catch(error => {
      console.error(error);
    });
});
