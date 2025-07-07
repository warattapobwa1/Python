'''Global Variables is variables that are created outside function everyone can use, both outside and inside
'''
x = "Warattapob"
def myfunc():
    print("My Name is",x)
myfunc()    
#global variable if in function declare local variable function will use local variable in function first
a = "Awesome"
def Myfunc():
    a = "kuy"
    print("Python is " + a)
Myfunc()    
print("Python is "+a)
#The global Keyword
'''
created varibles in function will called "local variable" and can only use
inside function
use global keyword to creted global variable
'''
def example():
    global A
    A = "fantastic"
example()
print("Python is",A)