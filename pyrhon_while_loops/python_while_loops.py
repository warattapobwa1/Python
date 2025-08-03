def test_one():
    i = 1
    while i < 6:
        print(i)
        i += 1 #increment of i if not have loop will continue infinty
print("Test one")
test_one()

#Break Statement
def test_two():
    i = 1
    while i < 6:
        print(i)
        if i == 3:
            break
        i += 1
print("Test two")
test_two()

#Continue Statement
def test_three():
    i = 0
    while i < 6:
        i += 1
        if i == 3: #When use continue will skip loop 3
            continue
        print(i)
print("test three")
test_three()

#else Statement
def test_four():
    i = 1
    while i < 6:
        print(i)
        i += 1
    else:
        print("i is no longer less than 6")
print("test four")
test_four()