"""
Dice rolling simulator
"""

from random import  randint
from time import sleep
a = randint(1, 6)

for i in range(1, 6):
    print("Rolling the dice")
    print()
    for l in range(a):
        print("*")
        sleep(0.1)
    print()
    print(a)
    break


