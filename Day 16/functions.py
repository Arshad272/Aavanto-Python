# Types of functions

# 1. Function without arguments and without return statement

def greet():
    print("Hello, good evening!")
# greet()

# 2. Functions with arguments and without return statement
def div(a, b):
    d = a / b 
    print(d) 

# div(6,2) 

# 3. Functions without arguments and with return statement

def return_something():
    a = 523
    return a 
# return_something() 
# print(return_something())
x = return_something() 
# print(x) 

l = [8,89,877,98,56,45]
# print(len(l) ) 
x = len(l)
# print(x) 

# 4. Functions with arguments and with return statement

def add(a, b):
    addition = a + b
    return addition

# print(add(30, 20)) 


# Default Parameters

def add(a = 10, b = 0):
    return a + b 
# print(add(10, 20)) 
# print(add()) 


# args -> if we place a '*' before parameter name then that parameter will accept multiple arguments from function call 
def multiple_arguments(*args):
    print(args)
    print(type(args)) 

# multiple_arguments(100,200,300,400,500)  


# kwargs - key word arguments
# you need to place two stars before parameter name. 
def dictionary(**d):
    print(d)
# dictionary(first = 'abcd', second = 'efgh')

# def dictionary(d):
#     print(d)

# dictionary({'first': 'abcd', 'second': 'efgh'})


def print_params(a, b, c):
    print(f"The value stored in a is {a}, b is {b} and c is {c}")

# print_params(b = 10, a = 20, c = 30) 


def add(a,b):
    print("The sum is : ") 
    return a + b
    print("Function Ended") 

# print(add(10,20)) 



