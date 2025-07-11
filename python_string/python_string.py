#String in python surrounded by eithrt single or double quot.
#'hello' is the same as "hello"
print("hello")
print('hello')

#You can use quot inside a string, as long as they don't match the quot surrounding the string.
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

#assign string to valuable
a = 'hello'
print(a)

#Multiline string, by use three double quot.
b = """hello my name is warattapob waiarsa,
i am come from thailand,
i study at kku university"""
print(b)

#string are arrays.
x = 'hello, world!'
print(x[1])

#looping through a string.
for c in 'banana':
    print(c)

#string lenght.
print(len(a))

#check string.
txt = "the best things in life are free!"
print("free" in txt)

#use if
tx = "The best things in life are free!"
if "free" in tx:
  print("Yes, 'free' is present.")

#check if not
text = "The best things in life are free!"
print("expensive" not in text)

#use if.
text1 = "The best things in life are free!"
if "expensive" not in text1:
  print("No, 'expensive' is NOT present.")