# OOP - Object Oriented Programming

# 1 Why do we need programming?
# We solve real world problems

# Everything in this world is made up of objects
# So, we need objects in programming also

# Objects are manufactured using blue print
# We call the blue print as class

# Class -> Blue print of a object
# Object -> It is a real world entity, instance of class

# a = 10
# print(type(a))

# Everyting in python is madeup of object oriented programming

# syntax:
# for creating a class
# class name_of_class :
#     code
#     code
#     code

# for creating object
# object_name = ClassName()

# method == function

class Car:
    def showSpeed(self, speed):
        print("Speed is ", speed)

fortuner = Car()
# print(type(fortuner))
# Car.showSpeed(fortuner, 150)
fortuner.showSpeed(150)
thar = Car()
# Car.showSpeed(thar, 170)
# thar.showSpeed(170)

marks = [50,60,50,540,50]
# print(type(marks))
marks.append(40)
print(marks)
  