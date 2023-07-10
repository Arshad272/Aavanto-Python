# Multilevel Inheritance in Python is a type of Inheritance that involves inheriting a class that has already inherited some other class

# class A:
#    code
# class B:
#    code
# class C(A, B): 
#    code

class Father:
    def car(self):
        print("I got a Car")
class Mother:
    def scooty(self):
        print("I got a Scooty")
class Child(Father, Mother):
    def cycle(self):
        print("I got a Cycle")

c = Child()
# c.cycle()
# c.car()
# c.scooty() 

f = Father()
f.car() 
# f.cycle() #Error