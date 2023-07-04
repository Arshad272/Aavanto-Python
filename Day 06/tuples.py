# Tuples

# Tuples are also used to store multiple values inside a single variable
# Tuples are represented by paranthesis -> ()
# Tuples are immutable -> i cannot modify contents of tuple 
# Tuples are heterogeneous 

# Syntax
# variable_name = (values, values)

tup = (10, 20, 30, "python", "hello", 10) 
# print(tup)
# print(type(tup))
# print(len(tup)) 

# Can we perform indexing and slicing in tuples?
# YES

# print(tup[1]) 
# print(tup[1:3])
# print(tup[-1])

# print(tup)

# print(tup.count(10))
# print(tup.index("python"))

t = (10, 20,60, (50, 900, 5000), [800,9000,500])
print(t[4][2])