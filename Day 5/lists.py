# Lists

# Lists are represented using Square Braces
# The elements inside lists are seperated by comma(,)
# Lists are heterogeneous, which means we can store different types of data inside lists
# Lists are mutable -> we can modify

# Syntax

# Variable_Name =  [  element1, elem2, elem3  ]

a = [10, 20, 30, 40, "string", 10.63, True]
# print(a)

# Indexing and Slicing

# Index Numbers
# Index numbers are used to access specific element from a list
# Index numbers start from 0 and end at (length of list - 1)
# list_name[ index_number  ]

# Positive index numbers
# a                   = [10, 20, 30, 40, "string", 10.63, True]
# positive_index_nums = [0,  1,  2,  3,   4,       5,     6]
# print(a[6])

# Negative index numbers 
# a =                  [10, 20, 30, 40, "string", 10.63, True]
# negative_index_nums =[-7, -6, -5, -4, -3,       -2,    -1]
# print(a[-6])

# Slicing
# Slicing is used to access multiple elements from a list
# syntax 
# list_name[ starting_index_num : ending_index_number ]
# print(a[ 1 : 4 ])

# print(type(a)) 

# Syntax 
# variableName.function_name()

# Append -> This append function is used to add element to the end of the list

a.append(900)
a.append("Python")
# print(a)

# Extend -> This is used to add multiple elements to list
b = ["aavanto", "technology", "python", "classes"]
# a.extend(b)
# print(a)

# '+' => similar to extend
a += b
# a = a + b
# print(a)

# insert => this is used to insert an element inside a list at specific position
a = [10, 20, 30, 40, "string", 10.63, True]
# a.insert(index_number, value/element)

a.insert(0 , 900)
# a = [900, 10, 20, 30, 40, "string", 10.63, True]
a.insert(2 , 6000)
# print(a)

# print(a[3])

# clear function will remove all elements from list
# a.clear()
# print(a)

# pop function will delete one element from the end of the list
# print(a)
# a.pop()
# print(a)

# index function is used to find the index number of an element
# print(a)
# print(a.index(10))

# reverse function is used to reverse a list
# print(a)
# a.reverse()
# print(a)

new_list = [10,80,60,70,10,50,30,44,6,55,10,222,333]
# count -> will return the count of an element inside a list
# print(new_list.count(10))

# sort -> used to sort a list 
# print(new_list)
# new_list.sort(reverse=True)
# print(new_list)


new_list = [10,80,60,70,10,50,30,44,6,55,10,222,333]
lst = new_list[3 : 6]
print(lst)
lst.reverse()
print(lst)