#Sample class with init method i.e. Constructor
class Person:

    #init method or Constructor:
    def __init__(self,name):
        self.name = name

    #sample method:
    def say_hi(self):
        print("Hello, my name is", self.name)

p = Person('Nikhil')
p.say_hi()
