# Loop through a List
# You can loop through the list items using  a for loop
fruits = ["Apple", "Banana", "Orange", "Pineapple", "Mango", "Coconut"]
for i in fruits:
    print(i)


# Use the range() and len() function to crate a suitable itirators
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])


# Using While Loop

i = 0
while i < len(fruits):
    print("While loop " + fruits[i])
    i = i + 1


# List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

# Or
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

newlist = [x for x in fruits if x != "apple"]

print(newlist)

#Iterable 
#The iterable can be any iterable object, like list,tuple,set etc.
#Also you can use range() to create an iterable.
newlist = [x for x in range(20)] 
print(newlist)

#Ex - Accept only numbers lower than 5

newlist=[ x for x in range(10) if x<5]
print(newlist)

#Expression
#set the values in the new list to upper case 

newlist=[x.upper() for x  in fruits]
print(fruits)

#Set all values in new list as hello
newlist = ['hello' for x in fruits]
print(newlist)

#Sort lists
