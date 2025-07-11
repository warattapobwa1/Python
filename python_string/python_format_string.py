#use f-string because we can not use operator + to combine string and number
age = 36
txt = f"My name is John, I am {age}"
print(txt)

#placeholders and modifiers
def price():
    price = 59
    txt = f"The price is {price} dollars"
    print(txt)
price()
def price_decimal():
    price = 59
    txt = f"The price is {price:.2f} dollars"
    print(txt)
price_decimal()
def price_operator():
    txt = f"The price is {20 * 59} dollars"
    print(txt)
price_operator()


