## Añadiendo un class constructor

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = 0
    
    def give_raise(self, amount):
        self.salary += amount

    def monthly_salary(self):
        return self.salary/12
        
emp = Employee("Korel Rossi",2500)
print(emp.name)
print(emp.salary)  

## Condicionantes dentro de una class

class Employee:
  
    def __init__(self, name, salary=0):
        self.name = name
        if salary>=0: 
            self.salary = salary 
        else: 
            print("Invalid salary!")
            self.salary = 0
      
emp = Employee("Korel Rossi", -1000)
print(emp.name)
print(emp.salary)

# from datetime import datetime
