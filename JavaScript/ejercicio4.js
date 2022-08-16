
// Ejercicio 4

/*- Una cadena de texto con tu Nombre

- Otra cadena de texto con tu Apellido 

- Una cadena de texto que se llame "estudiante" concatenando tu Nombre y tu Apellido con un espacio entre medias

- Una cadena de texto que se llame "estudianteMayus" que contenga la cadena estudiante pero todo en mayúsculas

- Una cadena de texto que se llame "estudianteMinus" que contenga la cadena estudiante pero todo en minúsculas

- Una variable que contenga el número de letras de la cadena "estudiante" contando los espacios

- Una variable que contenga la primera letra del Nombre

- Otra variable que contenga la última letra del Apellido

- Una cadena de texto que elimine los espacios de la variable "estudiante"

- Una variable booleana que diga si el Nombre está contenido en la variable "estudiante"
*/

let nombre='Bruno';
console.log(nombre);

let apellido='Pizzagalli';
console.log(apellido);

let estudiante=`${nombre} ${apellido}`;
console.log(estudiante);

let estudianteMayus=estudiante.toUpperCase();
console.log(estudianteMayus);

let estudianteMinus=estudiante.toLowerCase();
console.log(estudianteMinus);

let estudianteEspacios=estudiante.length;
console.log(estudianteEspacios);

let estudiantePrimerLetraNom=nombre.charAt(0);
console.log(estudiantePrimerLetraNom);

let estudiantePrimerLetraApe=apellido.charAt(0);
console.log(estudiantePrimerLetraApe);

let estudianteEliminaEspacio=estudiante.replace(/\s/g, '');
console.log(estudianteEliminaEspacio);

let estudianteVariableBoolean=estudiante.includes(nombre);
console.log(estudianteVariableBoolean);