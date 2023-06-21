# sets 
# In sets we are not allowed to perform indexing and slicing

# the elements of sets are not stored in contiguous memory locations

# sets are denoted by '{ }' 

s1 = {2,3,4,5, "hello", True, False, (1,2)}   
print(len(s1)) 
s2 = {5,6,7,8,9}
# print(s)
# print(s[0:5]) 

# print(max(s))  
# print(min(s)) 
# print(type(s)) 
# print(len(s))
 
#  union() will add elements present in two sets
s = s1.union(s2) 
# print(s)
# print(s1) 

# intersection() will return common elements in two sets
s = s1.intersection(s2) 
# print(s) 

# s1 is superset of s2 and s2 is subset of s1
s1 = {1,2,3,4,5,6}
s2 = {2,3,5}
# print(s1.issubset(s2)) 

# pop() function will delete a random element from set and it will return deleted element
# print(s1.pop())
# print(s1)  

# remove()  will delete specific element form set
# s1.remove(4)
# print(s1) 

# lst = (6,7,8, 1, 2)
# s1.update(lst)
# print(s1) 


# diff = s1.difference(s2)
# print(diff) 