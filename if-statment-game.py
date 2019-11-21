#To use green color,these colors will work only in *NIXs, if you want to run the code on windows, just remove these two lines::
G = '\33[92m'
# Red color:
R = '\33[91m'


n = str(R + "All we had is one simple rule you little shit, answer yes or no, \nif this is so hard for you, you really need some pro help !!") 
m = str(R + "you might ask yourself why he is so annoyed by my answer, well let me tell you why: \ni just started coding with python and i have no idea what im doing, \nits much easier for me to keep going with this stupid game when i know what your answer is")

print("Welcome to the most simple game in the whole world")
print()
print("""Now we will start playing !!! hooooooooooo only if you are ready""")

print()

s = input("So, are you ready (yes/no): ")

if s == "yes":
    print("here we go!!")
if s == "no":
   print(R + "Oh !! Fuck you !!!") ; quit()

print()

print("the game is simple, all you need to do is to answer yes or no")

print()

print("""Ah ...yes!! you need to write "yes" or "no" when the game asks you, don't be lazy you little shit""")

print()

a = input("do you know what is the purpose of this game: ")

if a == "yes":
   print(R + "Oh !!! you do ! you little shit, even i didn't know where all this is going to while writing this line") ; quit()
elif a == "no":
   print("ok! neither do I, see !! i know one more thing about you and you about me, let's see where all this shit will lead us")
else:
   print(n) ; print(m) ; quit()

print()

b = input("lets go to the next question \nDo you think this is a good game: ")

if b == "yes":
   print("man!! I already like you <3")
elif b == "no":
   print(R + "Go fuck yourself") ; quit()
else:
   print(n) ; print(m) ; quit()

print()

c = input("You are doing good man ! Congrats, Now things will get harder .... \nOk next question: Do you know what language i use to write this game: ")

if c == "yes":
   print("Good !!")
elif c == "no":
   print(R + "Well!! Go have a look at the source code, and come back to give it another try (if your life is so fucking booring and you have nothing else to do)") ; quit()
else:
   print(n) ; print(m) ; quit()

print("Now the moment of trueth")

print()

d = input("""What languge was used to write this stupid game ? now things are different, you need to choose one correct answer by typing the numer near it: (1)C++ (2)Python (3)C# (4)HTML (5)JavaScript: """)

if d == "1":
   print(R + "NOOOOO !! Bye Bye !!") ; quit()
elif d == "2":
   print("Ok! that was the right answer, I hope that wasn't just a good luck")
elif d == "3":
   print(R + "Nice try! Bye Bye") ; quit()
elif d == "4":
   print("Maaaan I really hope you were just kidding!!!! any way Bye Bye") ; quit()
elif d == "5":
   print(G + "Ooh someone is feeling lucky today !!" + R + "\nNoooooo you are not !! Fuck off") ; quit()
else:
   print(n) ; print(m) ; quit()

print()

q3 = input("to this quistion you need to give a wrong answer, giving the right answer will get you a 'Fuck off' sign and the game will exit and you will not be able to play it again I mean never ..... (Just kidding I'm not that good), \nDo you belive in God: ")

if q3 == "yes":
   print(R + "there is no right and wrong answers for this question, but any way the game will exit just because im running out of ideas") ; quit()
elif q3 == "no":
   print(R + "there is no right and wrong answers for this question, but any way the game will exit just because im running out of ideas") ; quit()
else:
   print(n) ; print(m) ; quit()

