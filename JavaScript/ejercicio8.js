/*
Crea un archivo JS que contenga las siguientes líneas

- Una función sin parámetros que devuelva siempre "true"

- Una función asíncrona que utilice un setTimeout y pase por consola un "Hola soy una promesa" 5 segundos después de haberse ejecutado

- Una función generadora de índices pares automáticos
*/

function funcionSinParametros() {
    return true;
}

function funcionAsync() {
    setTimeout(() => {
        console.log("Hola soy una promesa");
    }, 5000);
}

function* generadorIndicesPares() {
    let i = 0;
    while (true) {
        yield i;
        i += 2;
    }
}

const sinp = funcionSinParametros();
const async = funcionAsync();
const gen = generadorIndicesPares();

console.log(sinp);
console.log(async);
console.log(gen.next().value);
console.log(gen.next().value);
console.log(gen.next().value);
console.log(gen.next().value);
console.log(gen.next().value);




