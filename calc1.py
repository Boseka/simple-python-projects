# This is a simple calculator written in python:

# Defining colors:
G = '\033[32m'
R = '\033[31m'
W = '\033[m'
Y = '\033[33m'
HG = '\033[42m'

while True:
    print()
    print(Y, "'This is a simple calculator written in Python'", W)
    print(G)
    print("Here's How it works ......")
    print("If you want to ADD two numbers, Enter 'add'")
    print("If you want to SUBSTRACT two numbers, Enter 'sub'")
    print("If you want to MULTIPLY two numbers, Enter 'mul'")
    print("If you want to DIVIDE two numbers, Enter 'div'")
    print("If you want to RAISE the frsi number to the power of the second number, Enter 'raise'")
    print("If you want to run MODULO DIVISION, Enter 'mod'")
    print("If you want to run FLOOR DIVISION, Enter 'floor'")
    print("if you want to QUIT, Enter 'quit'")
    print(W)
    user_input= input("Enter what kind of operation you want to do: ")

    if user_input == "quit":
        break
    elif user_input == "add":
        num1= float(input("Enter first number: "))
        num2= float(input("Enter second number: "))
        result = (num1 + num2)
        print(HG, num1, "+", num2, "=", result, W)
    elif user_input == "sub":
        num1= float(input("Enter first number: "))
        num2= float(input("Enter second number: "))
        result = (num1 - num2)
        print(HG, num1, "-", num2, "=", result, W)
    elif user_input == "mul":
        num1= float(input("Enter first number: "))
        num2= float(input("Enter second number: "))  
        result = (num1 * num2)
        print(HG, num1, "*", num2, "=", result, W)
    elif user_input == "div":
        try:
            num1= float(input("Enter first number: "))
            num2= float(input("Enter second number: "))
            result = (num1 / num2)
        except ZeroDivisionError:
            print(R + "An error occurred due to zero division", W)
        print(HG, num1, "/", num2, "=", result, W)
    elif user_input == "raise":
        num1= float(input("Enter first number: "))
        num2= float(input("Enter second number: "))
        result = (num1 ** num2)
        print(HG, num1, "**", num2, "=", result, W)
    elif user_input == "mod":
        num1= float(input("Enter first number: "))
        num2= float(input("Enter second number: "))
        result = (num1 % num2)
        print(HG, num1, "%", num2, "=", result, W)
    elif user_input == "floor":
        num1= float(input("Enter first number: "))
        num2= float(input("Enter second number: "))
        result = (num1 // num2)
        print(HG, num1, "//", num2, "=", result, W)
    else:
        print()
        print(R + "!!! Unknown input, Please read 'How it works section'!!!", W)
        print()

"""
I think we can reduce the code using Functions:

def fun1(x, y)
    num1= float(input("Enter first number: "))
    num2= float(input("Enter second number: "))
"""
