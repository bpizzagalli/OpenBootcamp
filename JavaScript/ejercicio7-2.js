/*
Crea un archivo llamado objetos.js que contenga las siguientes líneas

- Un objeto con tus datos personales (nombre, apellido, edad, altura, eresDesarrollador)

- Una variable que obtenga tu edad a partir del objeto anterior

- Una lista que contenga el objeto con tus datos personales y un nuevo objeto con los datos personales de tus dos mejores amig@s

- Una nueva lista con los objetos de la lista anterior ordenados por edad, de mayor a menor
*/


var objeto = {nombre:'Bruno',
                apellido:'Pizzagalli',
                edad:21,
                altura:1.78,
                eresDesarrollador:true};

var edad = objeto.edad;
console.log(edad);

listaDatos=[objeto];
listaDatos.push({nombre:'Juan',
                apellido:'Mejoramigo1',
                edad:21,
                altura:1.52,
                eresDesarrollador:true});
listaDatos.push({nombre:'Hola',
                apellido:'Mejoramigo2',
                edad:20,
                altura:1.54,
                eresDesarrollador:true});

console.log(listaDatos);

listaDatos.sort(function(a,b){
    return a.edad - b.edad;
});
console.log(listaDatos);