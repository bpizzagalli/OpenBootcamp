
/*
Crea un archivo JS que contenga las siguientes líneas

- Una variable que contenga la lista de la compra (mínimo 5 elementos)

- Modifica la lista de la compra y añádele "Aceite de Girasol"

- Vuelve a modificar la lista de la compra eliminando "Aceite de Girasol"

- Una lista de tus 3 películas favoritas (objetos con propiedades: titulo, director, fecha)

- Una nueva lista que contenga las películas posteriores al 1 de enero de 2010 (utilizando filter)

- Una nueva lista que contenga los directores de la lista de películas original (utilizando map)

- Una nueva lista que contenga los títulos de la lista de películas original (utilizando map)

- Una nueva lista que concatene la lista de directores y la lista de los títulos (utilizando concat)

- Una nueva lista que concatene la lista de directores y la lista de los títulos (utilizando spread operator)
*/

const listaCompra=[
    'leche',
    'pan',
    'harina',
    'azucar',
    'aceite'
];

listaCompra.push('aceite de girasol');
console.log(listaCompra);
listaCompra.pop();
console.log(listaCompra);

listaPeliculas=[
    {titulo: 'pelicula1', director: 'director1', fecha: '01/01/2010'},
    {titulo: 'pelicula2', director: 'director2', fecha: '02/01/2010'},
    {titulo: 'pelicula3', director: 'director3', fecha: '03/01/2010'}
];

const listaPeliculasPosteriores= listaPeliculas.filter(obj => obj.fecha>'01/01/2010');
console.log(listaPeliculasPosteriores);

const listaPeliculasDirectores= listaPeliculas.map(obj => obj.director);
console.log(listaPeliculasDirectores);

const listaPeliculasTitulos= listaPeliculas.map(obj => obj.titulo);
console.log(listaPeliculasTitulos);

const listaPeliculasDirectoresTitulos= listaPeliculasDirectores.concat(listaPeliculasTitulos);
console.log(listaPeliculasDirectoresTitulos);

const listaPeliculasDirectoresTitulosSpread= [...listaPeliculasDirectores, ...listaPeliculasTitulos];


