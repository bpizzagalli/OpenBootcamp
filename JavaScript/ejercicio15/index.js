const nombre = 'Bruno';
const apellido = 'Pizzagalli';

const objetoPersona = {
    nombre,
    apellido,
};

sessionStorage.setItem('persona', JSON.stringify(objetoPersona));
localStorage.setItem('persona', JSON.stringify(objetoPersona));

console.log(sessionStorage.getItem('persona'));
console.log(localStorage.getItem('persona'));



document.cookie = "persona=" + JSON.stringify(objetoPersona) + ";expires=" + new Date(Date.now() + 120000).toUTCString();


console.log(objetoPersona);