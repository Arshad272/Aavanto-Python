
# Create a Strong Password Generator

try :
    import random
    from time import sleep

    sleep(2) 
    pass_chars = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~!@#$%^&*()_+}{|:>?<,./}'''

    purpose = input("For which website/app you need password: ")
    length = int(input("Enter the lenght of password you want: "))

    # We need to create a passwords.txt file
    # amazon , 10 
    # Your password for amazon is :
    # P1/-R6)&zS

    password = ""
    for i in range(length):
        char = random.choice(pass_chars)
        password = password + char 

    print(f"\nThe password for {purpose} is : \n{password}\n")

    # with statement
    # With statement will take care of closing your file. 

    # syntax: 
    # with open() as variable_name:
    #     code
    #     code
    #     code
    # code
    # file = open("x.txt", "a")
    # file.close()
    with open("Passwords.txt", "a") as file :
        file.write(f"\n\nThe password for {purpose} is : \n{password}\n\n")

    print("The passwords are strored in passwords.txt file")
    sleep(10) 


except Exception as e :
    print(e)
    sleep(10) 