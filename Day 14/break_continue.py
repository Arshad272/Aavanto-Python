# Break key word is used to terminate a loop in python
for i in range(1, 11):
    print(i)
    if i == 5:
        break
   
# continue -> if you want to end the current iteration and starts next iteration
for i in range(1, 11):
    if i == 4:
        continue
    print(i)

# pass -> will do nothing
for i in range(1,6):
    if i == 2:
        pass
    print(i)

if 1 < 5:
    pass

print("Hello")