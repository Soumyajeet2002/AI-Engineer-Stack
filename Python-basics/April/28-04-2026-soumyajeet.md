# Assign Multiple Values to single Variable

## Many Values to Many Variables
- python allows us to assign values to multiple variables in on line.

```
x , y , z = "orange" , "apple" , "cheery"
print(x)
print(y)
print(z)

-> output:
orange
apple
cheery
```

## One value to multiple variables
- We can even assign the same value to multiple variables in one line.

```
x = y = z = " Orange "
print(x)
print(y)
print(z)

-> this prints 

orange
orange
orange

```

## Unpack a collection 
- if we have a collection of values in a <b>list</b> , <b>tuples</b> , etc . Python allows us to extract the values into variables. This is called Unpacking.

```
Unpack a list:

fruit = ["apple" , "banana" , "cherry"]
x , y , z = fruit

print(x)
print(y)
print(z)

-> this prints -> 
apple
banana
cheery

```

# Output Variable
# Global Variables 

## Global Varibales 
- Variables that are created outside of a function are known as the <b>Global Variables</b>

```
x = " awesome "

def myfunc():
    print("python is" + x)

myfunc()

-> this prints -> python is awesome
```
## Global Variable and Local Variable

- if we create a variable with the same name inside a function its called <b> Local Variable </b>
```
x = "Jeet"       -> this is the global varibale

def myName():

    x = "Soumyajeet"    -> is defines the local variable
    print("My name is:" + x)

myName()
print("my name is: " + x )  -> this prints Global variable

```