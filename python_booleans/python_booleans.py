#Boolean values have two values true and false
print(10 > 9)
print(10 == 9)
print(10 < 9)

def example():
    a = 200
    b = 33
    if b > a:
        print("b is greater than a")
    else:
        print("b is not greter than a")
example()

#evaluate values and variables
print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#most values are true almost any values is evaluate to true 
#if has some sort of content 
#any string is true except empty string
#any number is true except 0
#any list tuple set dictionaly are true except empty ones
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#functions can return a boolean
def myFunction() :
  return True
print(myFunction())

def my_Function() :
  return True

if my_Function():
  print("YES!")
else:
  print("NO!")

#check if an objects is an integer or not by using isinstance
k = 200
print(isinstance(k, int))