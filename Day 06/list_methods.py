a = [10, 30, 20, 30, "hello",30, "world", False, 20.65, 30]
# print(a.count(30))
# remove() -> reomove function is used to delete an element from list

# print(a)
# a.remove(30)
# print(a)

# Can we store a list inside a list?

lst = [10, 20, 30, ["hello", "python", True, 500], "aavanto", 99]
# syntax for accessing elements inside sublist.
# list_name[index_number_of_sublist][index_number_element_in_sublist]
# print(lst[3][3])

# print(type(lst))

# len function in python is used to find out the count of elements inside list or to find out the length of the list
# print(len(lst))

# print(lst[0])

# Can i modify an element inside a list using index number?
# YES
# print(a)
# syntax
# list_name[index_number] = new_value
lst[0] = 999
lst[2] = 300
# print(lst)

# copy function -> it is used to copy the elments from one list to another list

a = [10, 30, 50]

b = a.copy()

# print(b)

# extend function -> will take a list or string as input parameter

a = [10, 30, 20, (500, "hello")]
# a.extend(["hello"])
print(a[3][1])
