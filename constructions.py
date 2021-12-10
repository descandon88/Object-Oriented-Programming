import math
# Write the class Point as outlined in the instructions
class Point: 
    def __init__(self,x=0,y=0):
        self.x = x
        self.y =y

    def distance_to_origin(self):
      
       return math.sqrt(self.x**2 + self.y**2)

    def reflect(self,axis):
        if axis == "x":
            self.y = -self.y
        if axis == "y":
            self.x =-self.x
        else :
            print('Error messaje!')

pt = Point(x=3.0)
pt.reflect("y")
print((pt.x, pt.y))
pt.y = 4.0
print(pt.distance_to_origin())

###ALTERNATIVE CONSTRUCTORS

class Player:
    MAX_POSITION = 10
    
    def __init__(self):
        self.position = 0

    # Add a move() method with steps parameter     
    def move(self, steps):
        if self.position + steps < Player.MAX_POSITION:
           self.position = self.position + steps 
        else:
           self.position = Player.MAX_POSITION
    
    # This method provides a rudimentary visualization in the console    
    def draw(self):
        drawing = "-" * self.position + "|" +"-"*(Player.MAX_POSITION - self.position)
        print(drawing)

p = Player(); p.draw()
p.move(4); p.draw()
p.move(5); p.draw()
p.move(3); p.draw()
