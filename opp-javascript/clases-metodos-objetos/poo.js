// Clase de Clases, métodos y Objetos


function Persona (nombre, edad, dni) {
    this.nombre = nombre;
    this.dni = dni;
    this.edad = edad;
    // console.log("Hola, soy "+nombre + "con dni "+ dni);
    this.getDni = function () { 
        return this.dni;
    }

    this.saludar = function () {
        console.log("hola soy "+this.nombre + " tengo " + this.edad + " años y mi DNI es "+ this.dni);
    }
}

let objetoPersona = new Persona("Marko",32, 63838070); // creacion de una instancia llamado "Persona"

console.log(objetoPersona.getDni());
console.log(objetoPersona.saludar());