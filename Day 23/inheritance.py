# class Student:
#     def __init__(self, name, age):
#         self.studentName = name
#         self.studentAge = age

#     def showDetails(self):
#         print(f"The name of student is {self.studentName} and age is {self.studentAge}")

# class Laptop(Student):
#     def showSpecs(self, details):
#         print(f"Laptop specs are {details}")

# s1 = Student("Elon Musk", 50)
# s2 = Student("Mark Zuck", 40)
# s1.showDetails()
# l1 = Laptop()
# l1.showDetails()
# l1.showSpecs("i5 8th Gen")


# inheritance
# sytnax:
# class ChildClassName(ParentClassName):
#     code
#     code
#     code

class A:
    def __init__(self):
        print("In class A")
    def showClass(self):
        print("The showclass method of class A")

class B(A):
    def __init__(self):
        print("In class B")
    def showName(self):
        print("This method belongs to class B")

# aObj = A()
bObj = B()

bObj.showName()
bObj.showClass()
