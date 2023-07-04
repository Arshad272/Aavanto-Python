# Dictionaries are key value pairs in python
# Keys and Values are separated by colen and key value pairs are separated by comma 
# Dictionaries doesn't allow duplicte keys 
# Syntax : {"key" : "value", "key" : "value" etc...}

d = {1: "hii",  2 : "two", 3: "three"} 
# print(d) 
# print(type(d)) 
# print(d[1]) 
# dict_name[key] = new_element
d[1] = "python"
d[4] = "program" 
d.update({"5": "Five", "6": "Six"}) 
# print(d) 

new_d = { "key1" : [45,12,89,56], "key2" : "programming", "key3" : "is best" }
# print(new_d)

# values() -> will return all the values present inside a dictionary
# print(new_d.values()) 

# keys() -> will return all the keys present inside a dictionary
# print(new_d.keys()) 

# print(new_d.get("key2")) 
# print(new_d["key4"]) 

# new_d.pop("key2")
# print(new_d)
 
# new_d.popitem()
# print(new_d) 

# print(new_d.items())


 

