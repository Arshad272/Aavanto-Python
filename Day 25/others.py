# eval()
# It is used to evaluate string based expressions
# 10 + 9 / 5 * 9
# x + y + 2z 
# x + 2 * y + z / 5
x = 10
y = 15
z = 20
# print(eval("x + 2 * y + z / 5")) 
# x + 2 * y + z / 5
# 10 + 2 * 15 + 20 / 5
# 10 + 2 * 15 + 4.0
# 10 + 30 + 4.0 
# 44.0 
# DMAS - Division, Multiplication, Addition, Subtraction
a = 10
b = 20
# print(eval("a + b")) 

# id()
# It returns the address of a variable
a = 10
# print(id(a)) 

# List Comprehensions
# It's a short form syntax for declaring a list

# lst = []
# for i in range(1, 101):
#     lst.append(i)
# print(lst) 

# syntax:
# variable_name = [var for var in range(args)]
# lst = [z for z in range(1, 101)] 
# print(lst)

# lst = []
# for i in range(1, 101):
#     if i % 2 == 0:
#         lst.append(i)
# print(lst) 

lst = [i for i in range(1, 101) if i % 2 == 0]
# print(lst) 

age = int(input("Enter age: "))
# if age > 18:
#     print("Eligible")
# else:
#     print("Not eligible")

# variable = "str 1" if condition else "str 2"
eligibility = "Eligible" if age > 18 else "Not Eligible"
# print(eligibility)