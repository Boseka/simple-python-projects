"""
Hello, here are some functions and modules

Written in python with love, by Boseka !!!
"""

#The first function which prints "first function called successfully" when it's called
print("FIRST FUNCTION:")
def func1():
    print("first function called successfully")

func1() #calling the first function 

print()
#Defining variables once so we don't need to define them every time we define new function
x = int(input("first number (x):"))
y = int(input("second number (t):"))
z = int(input("interval (z):"))
a = list(range(x, y, z))

print()

#The second function that creates a list from x to y with range of z and does some simple list operations 
def func2(x, y, z):
    print(a)
    print("the list contains items:", len(a))
    print("the max value in the list:", max(a))
    print("the min value in the list", min(a))
    print("the average number is:", sum(a) / len(a))

print()
print("SECOND FUNCTION:")
func2(x, y, z)  #calling the second function with x, y, z as variables

#The third function which compares x and y values
def func3(x, y):
    print("the first number is:", x)
    print("the second number is:", y)
    if x >= y:
        print(x, ">=", y)
        return x
    else:
        print(x, "<=", y)
        return y
print()
print("THIRD FUNCTION")
func3(x, y)  #calling 3d function 
print()

#The modules part
#importing pi function from math module and printing pi value
from math import pi
print("print pi from math module, pi =", pi)

print()

#Importing randint function from random module ans printing numbers between x and y in random order
from random import randint
print("Random numbers between x & y")
for i in range (y):
    print(randint(x, y))

#Thank you, leave a like if this was helpful !
