# EJERCICIO #1
# Creando mi primera Clase

class Employee:
    def set_name(self, new_name):
        self.name= new_name

emp = Employee()

emp.set_name('Korel Rossi')

print(emp.name)


# EJERCICIO #2

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

# EJERCICIO #3
# Using attributes in class definitation
# Add a method give_raise() to Employee that increases the salary by the amount passed to give_raise() as a parameter.

class Employee: 
    def set_name(self, new_name):
        self.name = new_name
    
    def set_salary(self, new_salary):
        self.salary=new_salary

    def give_rise(self, rise_amount):
        self.salary = self.salary + rise_amount
    
    def monthly_salary(self):
        return (self.salary)/12


emp= Employee()
emp.set_name('Oscar Andrade')
emp.set_salary(50000)

print(emp.salary)
emp.give_rise(1800)
print(emp.salary)

monthlySalary = emp.monthly_salary()

print(monthlySalary)
