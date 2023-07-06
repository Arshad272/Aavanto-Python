# Creating our own error
# raise -> for creating a error
# syntax:
# raise Exception("Error Message")
# import aavanto -> error

try:
    n = int(input("Enter a positive number: "))
    if n < 0: 
        raise ValueError("Negative numbers are not allowed! Enter only Positive Numbers...")
    else:
        print("Success")

except ValueError as e:
    print(e)
    