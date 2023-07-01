# Recusive Function?
# If a function call is present inside function definition iteself, then it is called as recursive function

# syntax:
# def function_name(parms):
#     code
#     function_name(args)
# function_name(args)

# def recursion():
#     print("hello") 
#     recursion() #This will return RecursionError
# recursion()


# Factorial of a number using recursion
# Factorial(n) -> multiplication of all the numbers from 1 to n
# for eg.: factorial of 5 is -> 1*2*3*4*5 -> 120

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
# 0. factorial(4) 
# 1. 4 * factorial(3)   -> 4 * 6 - 24
# 2. 3 * factorial(2)   -> 3 * 2 - 6
# 3. 2 * factorial(1)   -> 2 * 1 - 2

result = factorial(5)
# print(result)


n = int(input("Enter a number: "))
result = 1
for i in range(1, n+1):
    result = result * i
# result = 1 * 1 = 1 
# result = 1 * 2 = 2
# result = 2 * 3 = 6
# result = 6 * 4 = 24
# print(result) 

