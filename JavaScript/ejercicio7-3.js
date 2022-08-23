/*
Crea un archivo llamado fechas.js que contenga las siguientes líneas

- La fecha de hoy

- La fecha de tu nacimiento

- Un variable que indique si hoy es más tarde (>) que la fecha de tu nacimiento

- Una variable que contenga el día de tu nacimiento

- Una variable que contenga el mes de tu nacimiento (recuerda que Enero es mes 0)

- Una variable que contenga el año de tu nacimiento (con 4 dígitos)
*/

var fechaHoy = new Date();
console.log(fechaHoy);
var fechaNacimiento = new Date('2001-01-25');
console.log(fechaNacimiento);

if(fechaHoy > fechaNacimiento){
    console.log('Hoy es más tarde que la fecha de nacimiento');
}else{
    console.log('Hoy es antes que la fecha de nacimiento');
}

var diaNacimiento = fechaNacimiento.getDate();
console.log(diaNacimiento);
var mesNacimiento = fechaNacimiento.getMonth();
console.log(mesNacimiento);
var anioNacimiento = fechaNacimiento.getFullYear();
console.log(anioNacimiento);

