# Take elements of list as input from user
# perform sqaure opertion on list elements
# Display the output
lst = []
n = int(input("Enter the lenght of list:"))
while n >= 1:
    element = int(input("Enter element: "))
    lst.append(element)
    n -= 1

print(lst) 

sqare_nums = []
i = 0
while i < len(lst):
    # print(lst[i])  
    square = lst[i] ** 2  
    sqare_nums.append(square)
    i += 1  

print(sqare_nums)  