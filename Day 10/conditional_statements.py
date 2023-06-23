# if, elif (else if), else

# if -> if the condtion is true then the code present inside if block will get executed

# syntax:
# if ( condition ) :
#     code
#     code 

# if 10 > 5 :
#     print("Condition is correct") 
#     print("If block is getting executed")
#     print("Success")

# Checking the eligibility to Vote
# age = int(input("Enter Age: "))
# if age > 18:
#     print("You are eligible to Vote")
    
# print("Program Executed") 


# if - else
# if the condtion is true then the code present inside if block will get executed. Otherwise the code present in my else blok will get executed
# Syntax: 
# if condition : 
#     Code
#     Code
# else:
#     Code
#     Code

# if age > 18:
#     print("You are eligible to Vote")
# else:
#     print("You are not eligible to Vote")

# print("Program Executed") 

# we can use elif, if we want to check more than one condition
# Syntax:
# if condition:
#     code
# elif condition:
#     code
# elif condition:
#     code
# elif condition:
#     code
# elif condition:
#     code
# elif condition:
#     code
# else:
#     code

marks = int(input("Enter You Marks in Python: "))

if marks > 90:
    print("You got A Grade")
elif marks > 75:
    print("You got B Grade")
elif marks > 60:
    print("You got C Grade")
elif marks > 40:
    print("You got D Grade")
else:
    print("You are Failed") 

print("Program Executed")

# m1 = 20
# m2 = 18
# m3 = 15

# final_marks = m1 + m2 + m3
# print(final_marks)