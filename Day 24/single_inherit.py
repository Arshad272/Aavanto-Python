# In single inheritance we will have a parent class and a child class. Here a single child class will be inheriting a single parent class. 

# parent class / super class
# child class / sub class

class Student:
    def __init__(self, name, age):
        self.studentName = name
        self.studentAge = age
    def showDetails(self):
        print(f"The name of student is {self.studentName} and age is {self.studentAge}")
# super() is a built in function, with the help of this function we can access all the methods of parent class during inheritance 
# Syntax:
# super().parentClassMethodName(args)
class Laptop(Student):
    def __init__(self, name, age):
        print("In init method of Laptop Class")
        super().__init__(name, age)
    def showSpecs(self, details):
        print(f"Laptop specs are {details}")
    def xyz(self):
        super().showDetails()

# l1 = Laptop("Anand", 22)
# l1.showSpecs("i3 8th Gen")
# l1.showDetails()

l2 = Laptop("Adithya", 23)
# l2.showDetails() 
l2.xyz()