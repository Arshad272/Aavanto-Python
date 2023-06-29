
# Functions are used to do specific task
# Functions are block of code
# We can call functions multiple times
# We can define a function once and we can call it multiple times
# The code present inside a function will get executed only when we call a function

# def function_name(parms, params):
#    code
#    code
#    code
# code

# Function without arguments
def greet(): # Defining a function
    print("Hii")
    print("Welcome to python class")
    print("Learn and enjoy")

# greet() #calling a function

# Functions with arguments

def mul(n1, n2):
    mul = n1 * n2 
    print(mul)

# mul("hello ", "world")  
# a = int(input("Enter a value: "))
# b = int(input("Enter b value: "))
# mul(a, b)  


# def info(my_info):
#     print(my_info)

# info("Hii, my name is sujith")


# print(len([4,45,469,569,4])) 

# sujith()

def sujith(iterable):
    a = 0
    for i in iterable:
        a += 1
    print(a)

l = "python"
sujith(l) 


