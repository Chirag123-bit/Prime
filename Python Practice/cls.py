class Person:

    def __init__(self, name, age, address): #Dunder Method #Magic Method
        self.secretInt = "100"
        self.password = "mySecretPassword"
        self.name = name
        self.age = age
        self.address = address

    def funcOne(self):
        print(self.name)

    def funcTwo(self):
        print("hello world 2")

    def location(self):
        print("Lives in Nepal")
    
   


class PersonOfNepal(Person):

    def location(self):
        print("Lives in Nepal")

    

    def polyFunction(self,a=None, b=None): #Method Overloading
        if(a==None and b==None):
            print('Inside Task 1')
        elif(a!=None and b==None):
            print("Inside Task 2")
        else:
            print("Inside Task 3")



obj1 = Person(name="Chirag", age=30, address="Kathmandu")
obj2 = Person(name="Luchhen", address="Thankot",age=16)
obj3 = PersonOfNepal(name="Luchhen", address="Thankot",age=16)
obj3.polyFunction()
obj3.polyFunction("asdsd")
obj3.polyFunction("asdsd","sdsadad")

# obj3.funcOne()
# obj3.funcTwo()


# obj1.funcOne()
# obj1.funcTwo()

# obj2.funcOne()
# obj2.funcTwo()



print(10+2) #12
print("10"+"2") #102