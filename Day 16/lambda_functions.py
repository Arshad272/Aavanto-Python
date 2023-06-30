# lambda functions are also called as anonymous functions
# They are single line functions

# Syntax:
# variable_name = lambda parms,parms : expression

x = lambda a, b, c : a +  b + c
# print(x(4, 3, 6)) 
# 

l = lambda iterable : len(iterable)

# print( l( [56,89,56,5,23,3,254,7] ) ) 


d = lambda a , b = 10: a + b 

# print(d(10, 50)) 
