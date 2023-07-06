# 1. open a file 
# syntax: open(file_name, mode)
# 2. Read / Modify
# 3. Close

# r -> read mode, here we cannot modify a file
data = open("demo.txt", "r")
# print(data) 
# read() -> is used to read the contents of a file
# print(data.read())  

# readline() -> it is used to read a individual line
# print(data.readline(), end="")
# print(data.readline(), end="")
# print(data.readline(), end="")

# readlines() -> it will return all the lines from a file in a list format
# print(data.readlines())

# lst = []
# d = data.readlines()
# for i in d: 
#     lst.append(i.strip()) 
# print(lst) 

data.close()

# w mode -> it will create a new file, if the file is not present. It will delete contents of a file, if the file is already present
file = open("newfile.txt", "w")
file.write("Previous data was deleted")
file.close()

