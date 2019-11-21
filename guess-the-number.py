"""
The computer will think of a number, and the user will try to 
guess what number between 1-10
"""

#coloring the output, i think this will work only in *NIXs

G = '\033[32m'
R = '\033[31m'
W = '\033[m'

#Importing randint and sleep
from random import randint
from time import  sleep

print("The game is simple, I will think of a number between 1-10 and \nyou will try to guess what number I'm thinking of")
print()

#Generating random number
for i in range(1, 10):
    a = int(randint(1, 10))

#The user's guess
b = int(input("Guess the number:"))

#The result
if a == b:
    print(G + "Yes!!! You did it, the number i was think of is:", W, a)
else:
    print(R + "Nops, Sorry !!! that's the wrong answer, i was thinking of:", W, a)

#Quit
print()
print("Quitting")
for i in range(5):
    print(".")
    sleep(0.1)

