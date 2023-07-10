# Here, more than one child class can inherit from same parent class
# class A:
#    code
# class B(A):
#    code
# class C(A):
#    code

class Father:
    def bike(self):
        print("I got a Bike")
class Brother1(Father):
    def bigCycle(self):
        print("I got a Big Cycle")
class Brother2(Father):
    def smallCycle(self):
        print("I got a small Cycle")

# b2 = Brother2()
# b2.smallCycle()
# b2.bike() 
# b2.bigCycle() # Error

b1 = Brother1()
b1.bigCycle()
b1.bike() 