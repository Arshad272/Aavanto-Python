
# the code inside else block will get exceuted if the loop is not terminating with break statement

# for i in range(1, 6):
#     if i == 44:
#         break 
#     print(i)
# else:
#     print("LOOP not terminated by BREAK") 

# a = "Hello "
# b = "World"

# print(a + b)
# print(a * 30) 

# n = int(input("Enter number of line: "))
# for i in range(1, n+1):
#     print("* " * i)  

# OUTPUT FOR ABOVE CODE
# * 
# * *
# * * *
# * * * *
# * * * * *

# n = int(input("Enter number of line: "))
# for i in range(n, 0, -1):
#     print("* " * i)  

# OUTPUT FOR ABOVE CODE
# * * * * * 
# * * * *
# * * *
# * *
# *

# n = int(input("Enter number of line: "))
# for i in range(1, n+1):
#     print("* " *10 ) 

# OUTPUT FOR ABOVE CODE
# * * * * * * * * * * 
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *

# Check whether the number is prime number or not

# n = int(input("Enter a number: "))

# for i in range(2, n):
#     if n % i == 0:
#         print(f"{n} is a not prime number")
#         break 
# else:
#     print(f"{n} is a prime number")

n = int(input("Enter a number: "))

# for i in range(1, n+1): 
#     for j in range(n, i-1, -1): # 4 , 3 , -1
#         print(j, end = " ")
#     print() 

# OUTPUT OF BELOW CODE
# 4 3 2 1
# 4 3 2 
# 4 3 
# 4 

