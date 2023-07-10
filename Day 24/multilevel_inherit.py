# In multilevel inheritance, a child class will be accessing all the methods of parent class and another child class will be inheriting the child class
# class A:
#    code
# class B(A):
#    code
# class C(B):
#    code

class GrandFather:
    def land(self):
        print("I got some land")
class Father(GrandFather):
    def house(self):
        print("I got a House")
class Child(Father):
    def bike(self):
        print("I got a bike")

# c = Child()
# c.bike() 
# c.house()
# c.land() 

# f = Father()
# f.house()
# f.land() 
# f.bike()  # Error

g = GrandFather()
g.land() 