'''
Variables can store data of different type.
Text type: str
Numeric types: int, float, complex
Sequence types: list, tuple, range
Mapping type: dict
Set type: set, frozenset
Boolean type: bool
Binary type: bytes, bytearray, memoryview
None type: Nonetype
'''
#Getting the data type
x = 5
print(type(x))
#setting data type
a = "Hello world" #str
b = 20 #int
c = 20.5 # float
d = 1j #complex
e = ["apple", "banana", "cherry"] #list
f = ("apple", "banana", "cherry") #tuple
g = range(6) # range
h = {"name":"first", "age": 22} #dict
i = {"apple", "banana", "cherry"} #set
j = frozenset({"apple", "banana", "cherry"}) #frozenset
k = True #bool
l = b"Hello" #bytes
m = bytearray(5) #bytearray
n = memoryview(bytes(5)) #memoryview
o = None #NoneType
#if you want to set specific data type use type(variables)