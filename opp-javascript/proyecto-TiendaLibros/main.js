// Tienda de libros que tiene una clase principal Book con su proiedades de Titulo, autor y precios


// class Book {
//     constructor(titulo, autor, precio) {
//         this.titulo = titulo;
//         this. autor = autor;
//         this.precio = precio;
//     }
// }

// class Seller {
//     constructor(){

//     }
// }

const _private = new WeakMap();
class Book {

    constructor(titulo, autor, precio) {
       const properties = {
         _titulo : titulo,
         _autor: autor,
         _price : precio
       }


       _private.set(this, {properties} );

    }
    // obtiene el titulo de un libro: 
    get titulo() {
        return _private.get(this).properties['_titulo'];
    }
    // setea/ modifica el titulo de un libro: 
    set titulo(nuevoTitulo) {
        return _private.get(this).properties['_titulo']=nuevoTitulo;

    }
}

class Comic extends Book {
    constructor(pepe, autor, price, ilustradores, personajes){
        super(pepe,autor,price);
        this.ilustradores = ilustradores;
        this.personajes=personajes;
    }
}



// Instancia de Book: 
const libro01 = new Book("Los Tres Mosqueteros", "Alejandro Dumas", 320);
const libro02 = new Book("Frankenstain", "G.O.", 350);
const comic01 = new Comic("The Killing Joke", 'A.M.',150,['Brian Bolland','John Higgins'],['El Guasón','Batman', 'Barbara Gordon','Red Hood'])

console.log(libro01);
console.log('con el private.get: '+libro01.title);
console.log(libro02.autor);

console.log(comic01);

console.log(comic01.titulo);
console.log(comic01.price);

console.log(comic01.ilustradores);




// class Book01 {
//     title="1984";
//     author="George Orwell";
//     price = 350;
// }

// const book01 = new Book01();

// console.log(book01);
// console.log(book01.title);
// console.log(book01.author);
// console.log(book01.price);
