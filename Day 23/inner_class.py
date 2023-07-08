# class inside a class
class A:
    def __init__(self):
        self.hello = self.B("Welcome to Aavanto")
        self.hello.showStatus()
    def showName(self):
        print("Inside class A")
    
    class B:
        def __init__(self, data):
            print(f"Data is : {data}")
        def showStatus(self):
            print("Inside Class B")


objA = A()
# objA.showName()
# syntax:
# object_name = OuterClassName.InnerClassName()

# objB = A.B("Welcome to Python Class")
# objB.showStatus()