# It is combination of multiple inheritance and hierarchical inheritance

# class A:
#    code
# class B(A):
#    code
# class C(A):
#    code
# class D(B, C):
#    code

class GrandFather:
    def horse(self):
        print("I got a horse")
class Father(GrandFather):
    def car(self):
        print("I got a Car")
class Aunt(GrandFather):
    def iPhone(self):
        print("I got a iPhone")
class Child(Father, Aunt):
    def cycle(Self):
        print("I got a Cycle")

# c = Child()
# c.cycle()
# c.car()
# c.horse()
# c.iPhone()

a = Aunt()
a.horse()
a.iPhone()
# a.car() #Error