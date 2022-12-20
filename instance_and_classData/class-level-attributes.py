# Define a class Player that has:
# A class attribute MAX_POSITION with value 10.
# The __init__() method that sets the position instance attribute to 0.
# Print Player.MAX_POSITION.
# Create a Player object p and print its MAX_POSITION.

class Player: 
    MAX_POSITION = 10
    def __init__(self, position=0):
        self.position=position

print(Player.MAX_POSITION)

p = Player()
print(p.MAX_POSITION)

# Add a move() method with a steps parameter such that:
# if position plus steps is less than MAX_POSITION, then add steps to position and assign the result back to position;
# otherwise, set position to MAX_POSITION.
class Player:
    MAX_POSITION = 10
    def __init__(self):
        self.position = 0

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

