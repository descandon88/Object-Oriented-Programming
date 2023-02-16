const Comida = {
    id: 1,
    nombre: 'Manzana',
    color: 'rojo',
} // declaracion de un objeto

// console.log(Comida);

// Metodos y Clases
class comida {
    constructor(id, nombre, color) {
        this.id = id;
        this.nombre = nombre;
        this.color = color;
    }
    // Se agrega el método nombrar
    nombrar () {
        return `${this.nombre} de color ${this.color}`;
    }
}

const manzana = new comida(1,'manzana','rojo');
const pera = new comida (2,'pera','verde');
console.log(manzana.nombrar());

console.log(pera);


// HERENCIA

class Galleta extends comida {
    constructor(id, nombre, color, sabor){
        super(id,nombre,color);
        this.sabor = sabor;
    }
    nombrarGalleta() {
        return `${this.nombre} sabor ${this.sabor}`;
    }
}

const apple = new comida(1,"manzana","rojo");
const pears = new comida(2,"pera","verde");

const oreo = new Galleta(3, "oreos", "negro", "chocolate");
console.log(oreo.nombrarGalleta());