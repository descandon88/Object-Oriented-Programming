# Creando mi primera Clase

class Employee:
    def set_name(self, new_name):
        self.name= new_name

emp = Employee()

emp.set_name('Korel Rossi')

print(emp.name)

# Añadiendo un nuevo método a la clase

class Employee:
    def set_name(self, new_name):
        self.name=new_name

    def set_salary(self, new_salary):
        self.salary=new_salary

emp = Employee()
# Agregr el nomnbre Sebastián dominguez en emp
emp.set_name('Sebastián Dominguez')
# Agregar salario de emp en 50000
emp.set_salary(50000)

print(emp.name)
print(emp.salary)


