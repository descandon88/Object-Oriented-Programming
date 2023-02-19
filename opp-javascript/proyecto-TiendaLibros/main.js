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
         _precio : precio
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

    get precio() {
        return _private.get(this).properties['_precio'];
    }
    // setea/ modifica el precio de un libro: 
    set precio(nuevoPrecio) {
        return _private.get(this).properties['_precio']=nuevoPrecio;

    }


}

class Comic extends Book {
    constructor(titulo, autor, precio, ilustradores, personajes){
        super(titulo,autor,precio);
        this.ilustradores = ilustradores;
        this.personajes=personajes;
    }
    addIllustrator(newIllustrator = []){
        this.ilustradores.push(newIllustrator)
    }
}



// Instancia de Book: 
const libro01 = new Book("Los Tres Mosqueteros", "Alejandro Dumas", 320);
const libro02 = new Book("Frankenstain", "G.O.", 350);
const comic01 = new Comic("The Killing Joke", 'A.M.',150,['Brian Bolland'],['El Guasón','Batman', 'Barbara Gordon','Red Hood'])

console.log(libro01);
console.log('con el private.get: '+libro01.titulo);
console.log(libro02.autor);

console.log(comic01);

console.log(comic01.titulo);
console.log('precio: '+comic01.precio);
// console.log(comic01.ilustradores);

comic01.addIllustrator('J.H');

console.log(comic01.ilustradores);

// Crear una clase SHOPPING CAR que nos ayude agregar productos a nuestra canastita de compras y que nos ayude a realizar los cálculo de lo que costaría los productos que se irían a agregar.  

class ShoppingCar {
    constructor(){
        this.products = [];
    }
    addProduct (units, price) {
        this.products.push(...Array(units).fill(price));
    }
    showProducts() {
        console.log(this.products);
    }

    calcTotal() {
        return this.products
        .map(precio => precio)
        .reduce ((ac,precio)=> ac+precio, 0);
    }

    ImprimirTicket() {
        console.log(`Total por pagar ${this.calcTotal()}`)
    }

}

const cart01 = new ShoppingCar();
cart01.addProduct(4,comic01.precio);
cart01.addProduct(3,libro01.precio);

cart01.showProducts();
cart01.calcTotal();
cart01.ImprimirTicket();

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
