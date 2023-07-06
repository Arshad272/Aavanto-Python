# Global variables
# This variables can be accessed anywhere in the program

# Local Variables
# The scope of this variables is limited to a particular block

# g = 10 

# def local():
#     print(g) 
# local()
# print(g) 


# g = 10 
# def local():
#     l = 80
#     print(g) 
#     print(l) 
# local()
# print(l) 


name = "Python"
# global variable_name
# If we want to make changes to a global variable inside our function, then we need to use global keyword
def NameChanger():
    global name 
    name = "Java"
    print(name)
NameChanger()
print(name)



