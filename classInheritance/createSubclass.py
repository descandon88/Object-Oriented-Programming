# Add an empty Manager class that is inherited from Employee.
# Create an object mng of the Manager class with the name Debbie Lashko and salary 86500.
# Print the name of mng.

class Employee:
  MIN_SALARY = 30000    

  def __init__(self, name, salary=MIN_SALARY):
      self.name = name
      if salary >= Employee.MIN_SALARY:
        self.salary = salary
      else:
        self.salary = Employee.MIN_SALARY
        
  def give_raise(self, amount):
      self.salary += amount      
        
class Manager(Employee):
    pass

mng = Manager(name="Debbie Lashko",salary=86500)

# Print mng's name

print(mng.name)