#Note the first item has index 0
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#-1 refers to the last item, -2 refers to the second last item etc.
print("Negative index:",thislist[-1])

#range of indexes
#start at index 2 (included) and end at index 5 (not included)
#By leaving out the end value, the range will go on to the end of the list
def mylist_one():
    thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    print(thislist[2:5])
    print(thislist[:4])
    print(thislist[2:])
mylist_one()

#Range of negative indexes
#Specify negative indexes if you want to start the search from the end of the list
def mylist_two():
    thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    print(thislist[-4:-1])
mylist_two()

#Check if item Exists
#To determine if a specified item is present in a list use the in keyword
def mylist_three():
    thislist = ["apple", "banana", "cherry"]
    if "apple" in thislist:
        print("Yes, 'apple' is in the fruits list")
mylist_three()