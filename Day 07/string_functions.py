a = input("Enter string 1: ")
# b = input("Enter string 2: ")

# len() -> will return the lenght or the number of charectres present inside a string
# print(len(a)) 

# Indexing
# print(a[0]) 
# print(a[-1]) 

# Slicing
# print(a[:4]) 


# + operation or concatenation
# print(a + b) 

# upper -> will convert all chars into upper case
# print(a.upper())

# lower -> will convert all chars into lower case
# print(a.lower()) 

# title -> will convert the first char of all words into upper case
# print(a.title())

# capitalize -> will convert only the first char in a sentence to upper case
# print(a.capitalize())

# count -> will return the count of occurences of a char or sequence in string 
# print(a.count('and'))

# endswith -> return boolean
# print(a.endswith("xyz"))

# startswith -> return a boolean
# print(a.startswith("aa"))

# find -> returns index number of a char
# print(a.find('x')) 

# find -> returns index number of a char
# print(a.rfind('x')) 
  
# index -> returns index number of a char
# print(a.index('abd'))

# index -> returns index number of a char
# print(a.rindex('abd')) 

# isalnum -> return boolean, this will return true if a string contains both alphabets and number 
# print(a.isalnum())

# isalpha() -> will return true if all the chars present inside string are alphabets
# print(a.isalpha()) 

# isnumeric() -> will return true if all the chars inside a string are numbers.
# print(a.isnumeric()) 

# print(True) 

# print(a.isnumeric(10)) 
print(a.index('4',0,3)) 

# a=(1,'he','e','l','l','o')
# print(a[1][1]) 