from Person_parentClass import Person_parentClass


class Student_childClass(Person_parentClass):
    pass

x = Student_childClass("Mike", "Olsen")
x.printname()