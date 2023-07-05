# Exception -> Error 
# It will cause abnormal termination of program

# Types Error 
# 1. Compile Time Error
# Syntax Error
# We can't handle compile time error
# print("Hello")
# if True 
#     print("Hii") 

# 2. Logical Error
# I will not get any error, instead i will get wrong output
# We cannot handle these errors
# This will occur due to mistake in programmers logic
# def add(a, b):
#     return a - b 
# print(add(10, 4))

# 3. Run time Error
# We can hadle this run time errors
# print("Hello world") 
# print(c)
# print("Hii world") 

# age = int(input("Enter age: "))
# if age  > 18:
#     print("Eligible to vote")
# else:
#     print("Not Eligible to vote")

# syntax:
# try:
#     code
#     code
#     code
# except Exception as e:
#     print(e)
#     code
#     code
#     code

# try: 
#     age = int(input("Enter age: "))
#     if age  > 18:
#         print("Eligible to vote")
#     else:
#         print("Not Eligible to vote")
# except Exception as e:
#     print("Invalid input number")
    # print(e) 
# print(5/ 0)
# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter a number: "))
#     print(a / b) 
#     # print(c)
# except ZeroDivisionError as e:
#     print("We can't divide with zero")
# except ValueError as e:
#     print("Enter a valid number")
# except NameError as e:
#     print("Invalid varaible")
# except Exception as e:
#     print("Unknown error")


# try - except - finally
# try:
#     code
#     code
# except Exception as e:
#     code
#     code
# finally:
#     The code present inside this block will get executed whether we have any error or if we don't have any error
#     code
#     code

# try :
#     print("File opened")
#     print(5 / 0)
    
# except Exception as e:
#     print(e) 

# finally:
#     print("File Close")
#     print("I will get executed no matter what!!!")


# try - except - else - finally
# try:
#     code
#     code
# except Exception as e:
#     code
#     code
# else:
#     If our try block is not encountering any error means, then the code present inside else block will get executed
#     code
#     code
# finally:
#     The code present inside this block will get executed whether we have any error or if we don't have any error
#     code
#     code

# try:
#     if 10 > 5 -> cannot handle
#         print("hii") 
# except Exception as e:
#     print(e) 
# try :
#     print("File opened")
#     print(5 / 2)
# except Exception as e:
#     print(e) 
# else:
#     print("No error found in try block") 
# finally:
#     print("File Close")
#     print("I will get executed no matter what!!!")

# try:
#     l = [10,20,30]
#     print(5 / 0)
#     print(l[20])
# except IndexError as e:
#     print("Invalid index number")   
# except Exception as e:
#     print("Some error occured")   

