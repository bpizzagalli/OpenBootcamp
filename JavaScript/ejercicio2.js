const nom = "Bruno";
const edad = "21";
const desarrollador = true;
const nacimiento = new Date(2001, 0, 24);
const libro={
    titulo: "El señor de los anillos",
    autor: "J.R.R. Tolkien",
    editorial: "Minotauro",
    fecha: new Date(1954, 11, 11)
};
console.log(`Hola, me llamo ${nom} y tengo ${edad} años.`);
console.log(`Yo soy un desarrollador ${desarrollador} y nací el ${nacimiento}`);
console.log(`El libro ${libro.titulo} fue publicado por ${libro.autor} en la editorial ${libro.editorial} en el año ${libro.fecha.getFullYear()}`);