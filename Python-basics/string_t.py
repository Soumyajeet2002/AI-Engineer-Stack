for x in "banana":
    print(" trupti"+x)


# string length
    
a="hello,world"
print(len(a))


# use on "in" phrase in a string 

txt=" the best things in life are free"
print("free" in txt)


# use in if 
txt=" the best things in life are free"
if "free" in txt:
    print("yes, 'free' is present") 



#to get the length of a string 
txt="hii this is trupti"
print(len(txt)) # it will give the complete lenghth of the string




#Check String
#To check certain phrase or character is present in a string,we can use the keyword in
txt="the best things in life are free"
print("free" in txt)


#using conditional if

if "free" in txt:
    print("yes, 'free' is present")



#Check if not
# check a certain character of pharse is not present in a string we can use the kayword not in

txt="nothing is free in life you have to create it free for yourself "
print("expensive" not in txt) # it will return true because expensive is not present in the string

if "expensive" not in txt:
    print("no, 'expensive' is not present")




# Slice String 
#Using Sliceing string we can return a range of characters by using the slice syntax. 
# Specify the start index and the end index, separated by a colon, to return a part of the string.
b="hello,World@"
print("the range of slice string"+b[2:5])



#Slice from start
#by leaving out the start index the range will start frrom the first character
text="Hiii am trupti an intelligent girl with a beautiful heart"
print("Slice from first  " + text[:5]) # it will return the first 5 characters of the string


#Slice to the end 
#By leaving out the end index the range will go to the end of the string 
test_msg="Hii python is a great language"
print(test_msg[5:]) # it will return the string from index 5 to the end of the string


#Negative indexing
#Use negative indexes to start the slice from the end of the string
print(test_msg[-5:-2]) # it will return the string from index -5 to -2



#Remove whitespace
#Whitespace is the space before and after a string.
#The strip() method removes any whitespace from the beginning or the end of a string.
txt="   hello,world   "
print(txt.strip()) # it will return "hello,world" without the whitespace


#Replace String
#A replace method replaces a string with another string
test_text="Hii this is trupti"
print(test_text.replace("trupti","Trupti")) # it will replace the word trupti with Trupti


#Split String
#The split() method splits a string into a list where each word is a list item
txt="welcome to the world of python"
print(txt.split(" ")) # It will split the string into a list of words using space as a separator



#String Concatenation Operator
#To concatenate, or combine two strings you can use + operatpor 
A="Hello"
B="World"
c=A+B
print(c) # it will return hellowolrd without space because we have not added space between them


#To add a space between them, add " ":
c=A+" "+B
print(c)

#String Methods
#String 


