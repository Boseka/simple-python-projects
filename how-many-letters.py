"""
A script to count how many characters user's input has
"""

#Defining colors
G= '\033[32m'
R = '\033[31m'
W = '\033[m'
P = '\033[101m'

#User input
a = input("enter the word here: ")

# The output
print(G + "Your input:", W, P, "'",a,"'", W, G + " contains:", R, len(a), G + "characters", W)
print()
#print different messages based on length 
if len(a) < 10:
    print(G + "The input is Short")
elif 10 < len(a) < 20:
    print("The input has middle length")
elif 20 < len(a) < 30:
    print(R + "The input is Long")
else:
    print(R + "The input is way too long !!")

#That's it !!!
