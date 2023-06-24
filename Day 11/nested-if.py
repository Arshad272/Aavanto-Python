# If i want to make a decision, based on another decision, Then i can use nested if

# Nested If means, the presence of if block inside another if block

# Syntax:
# if condition :
#     if condition:
#         code
#     elif condition:
#         code
#     else:
#         code
# elif condition:
#     code
# else:
#     code

# Check whether the number entered by the user is positive or negative

# number = int(input("Enter a number: "))
# if number >= 0:
#     if number == 0:
#         print("Number is 0")
#     else:
#         print("Positive number")
# else:
#     print("Negative number") 


# If the age is greater than 18 means user is eligible to vote, if age is greater than 90 means user is not allowed to vote, if age is less than 18 means user is not allowed to vote.

age = int(input("enter age: "))
if age > 18:
    if age > 90:
        print("User is not allowed to vote")
    else:
        print("User is allowed to vote")
else:
    print("User is not allowed to vote") 