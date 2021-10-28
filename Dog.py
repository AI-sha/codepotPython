class Dog:
    #class attributes
    attribute1 = "mammal"
    attribute2 = "Dog"

    #method
    def fun (self):
        print("I am a", self.attribute1)
        print("I am a", self.attribute2)


#Object instantiation
Rodger = Dog()

print(Rodger.attribute1)
Rodger.fun()

