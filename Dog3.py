# Python3 program to show that we can create
# instance variables inside methods

# Class for Dog
class Dog3:
    # Class Variable
    animal = 'dog'

    # The init method or constructor
    def __init__(self, breed):
        # Instance Variable
        self.breed = breed

    # Adds an instance variable
    def setColor(self, color):
        self.color = color

    # Retrieves instance variable
    def getColor(self):
        return self.color

# Driver Code
Rodger = Dog3("pug")
Rodger.setColor("brown")
print(Rodger.getColor())