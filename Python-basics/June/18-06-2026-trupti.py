# Lists are used to store multiple items in a single variable. Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
# list are created using square brackets.


list1=["appple","banana","cherry"]
list2=[1,2,3,4,5]

#list items are ordered,changable and and allow duplicate values.


#Lsit lenght

print(len(list1))

#List can contain diffferent data types .

list3=["apple",1,True]
print(list3)

#Acess list items
#list items are indexed and you can access them by referring to the index number.

print(list3[2])

#Negative indexing means start from the end. here -1 refers to the last item, -2 referes to the seccond item

print(list1[-2])

#Range of Indexes 
#by specifying  a range of indexes you can specify a range of items to be returned.
print(list1[0:2])
#The search will start at index 0 (included) and end at index 2 (not included).

#Check if items exists

fruits=list(("apple","banana","cherry","guavee","mango","grapes","orange","kiwi","watermelon","papaya","pomegranate","pear","peach","plum","apricot","coconut","fig","date","jackfruit","lychee"))
if "apple" in fruits:
    print("Yes apple is present in fruit list")

# To change the value of a specific item, refer to the index number:
fruits[1]="blackberry"
print(fruits)

#To insert a list item at a specified index , use the insert() method.

fruits.insert(2,"kiwi")

#To add an item to the end of the list, use the append() method .

fruits.append("apple")
print(fruits)
#Remove method remove specidied item 
#Pop method removes the specified index, (or the last item if index is not specified)
fruits.remove("guavee")
print(fruits)

fruits.pop(1)
print(fruits)

#To append the list items from one list to another list use extend() method.

