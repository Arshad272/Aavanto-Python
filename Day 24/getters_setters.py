# Getters:
# Are used to get the value

# Setters:
# Are used to set / update the values

class Student:
    def __init__(self, name, age):
        self.stuName = name
        self.stuAge = age 
    def getName(self):
        return self.stuName
    def getAge(self):
        return self.stuAge
    def setName(self, name):
        self.stuName = name 
    def setAge(self, age):
        self.stuAge = age 


# s1 = Student("Sam", 55)
# print(s1.getName())
# print(s1.getAge()) 

# s1.setName("Ram")
# s1.setAge(65)
# print(s1.getName())
# print(s1.getAge()) 



def sub(a, b):
    print(a - b)

def add(a, b, c):
    print(a+b+c)
sub(10, 5)
add(10,20, 50)



# Abstraction

# Means hiding implementation details and showing essential details to user