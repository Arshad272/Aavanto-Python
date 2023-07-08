# Constructor -> Constructor is a special method. The code present inside constructor will get executed automatically when we create a object.

# def __init__(self):
#    code
#    code
#    code

# namespaces
# it's the area where our variables get stored
# Class Variables / Static Variables
# The variables is presnet inside a class

# Instace Variables / Object variables
# These variables are present inside our constructor / init method 
# syntax:
# self.variable_name = value

class Phone:
    type = "Touch"
    def __init__(self, color, refreshRate, ram, storage):
        self.phoneColor = color
        self.phoneRR = refreshRate
        self.phoneRAM = ram
        self.phoneStorage = storage
        print(f"The color is {color}, Refresh rate is: {refreshRate}")
        # print(f"The color is {phoneColor}, Refresh rate is: {phoneRR}")
    def showSpecs(self):
        print(f"The color is {self.phoneColor}, Refresh rate is: {self.phoneRR}")
        print(f"The RAM is {self.phoneRAM}, Storage is: {self.phoneStorage}")

# color = "Red"
redmi = Phone("Red", "90 Hz", "8 GB", "256 GB" )
OnePlus = Phone("Blue", "120 Hz", "12 GB", "512 GB")
# print(Phone.type)
# print(iPhone.type)
# redmi.showSpecs()
# OnePlus.showSpecs()


# Encapsulation:
# Binding / Wrapping data/variables and methods

