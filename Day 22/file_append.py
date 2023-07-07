# "a" -> append mode. It is used to add data in a file
# It will create a file, if the file is not existing

file = open("demo.txt", "a")
# file.write("Hello , Welcome to day 22")
# file.write("This is append mode")
# file.write("\nWelcome to OOP class")
# file.write("\nThis will be in new line")
# file.write("\nThis is another line")
file.close()

# r, w, a
# r+, w+, a+
# r+ -> we can perform both read and write operations
# file = open("demo.txt", "r+")
# file.write("Hello world" )
# print(file.read())
# file.close()


# file = open("demo.txt", "w+")
# file.write("New File")
# print(file.read())
# file.close()

# a+
# file = open("demo.txt", "a+")
# file.write("\nNew File")
# print(file.read())
# file.close()

# r -> only read
# w -> only write
# a -> only append
# r+ -> Both read and write
# w+ -> Both write and read
# a+ -> Both append and read


file = open("demo.txt", "r")
# seek() -> It will move the pointer
# file.seek(4)
# print(file.read())
# print(file.readline())
# print(file.readline())
file.close()

