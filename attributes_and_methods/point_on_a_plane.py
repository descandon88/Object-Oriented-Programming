# Write the class Point as outlined in the instructions
# Define the class Point that has: Two attributes, x and y - the coordinates of the point on the plane;
# A constructor that accepts two arguments, x and y, that initialize the corresponding attributes. These arguments should have default value of 0.0;

import math 

class Point: 
    def __init__(self, x=0.0,y=0.0):
        self.x=x
        self.y=y

    def distance_to_origin (self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def reflect(self, axis=""):
        self.axis=axis
        if self.axis=="x":
            self.y=  -self.y
        elif self.axis=="y":
            self.x=  -self.x
        else:
            print("Error message")


pt = Point(x=3.0)
pt.reflect("y")
print((pt.x, pt.y))
pt.y = 4.0
print(pt.distance_to_origin())