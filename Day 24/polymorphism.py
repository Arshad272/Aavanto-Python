# Poly -  many
# morph - forms
# many forms

# Method Overloading
# Inside same class we will have more than one method with same name and different parameters
# It is not supported in python
class Mathematics:
    def add(self, a, b):
        print(a + b)
    def add(self, a, b, c):
        print(a + b + c)

# m = Mathematics()
# m.add(10, 20, 30)
# m.add(10, 20) # Error


# Mehtod Overriding
# We will have methods with same name in parent class and child class
# Child class method overrides / replaces the method of parent class
class Father:
    def vehicle(self):
        print("I got a Car")
class Child(Father):
    def vehicle(self):
        print("I got a Bike")
c = Child()
# c.vehicle() 

f = Father()
# f.vehicle() 
