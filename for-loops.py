# for loops, in action, by Boseka !!!!

#Introduction to the app:
print("Hello there !!!")
print("This is a simple app written with python to print all numbers in some range from x to y with z interval")
print()
#Our variables:
num1 = int(input("Enter the first number: "))  #The start number
num2 = int(input("Enter the second number: "))  #The ending number
interval = int(input("Enter the interval '!=0': "))  #The interval

if interval == 0:
    print("Error, interval should be grater than 0")
    print("Quitting ......")
    quit()    

list_results = list(range(num1, num2, interval))  #Creating a list with user input

print()

#For loop
for i in range(num1, num2, interval):
    print(i)
#For loop ends here
print()
#While loop
while True:
    print("Do you want to print the result as a list? (yes/no):")
    a = input("")
    print()
    if a == "yes":
        print(list_results)
        print()
        print("Thank you for using our application")
        break   #End while loop
    elif a == "no":
        print()
        print("Quitting ........")
        quit()   #Ending while loop, didn't use break, because i want to end the app here
    else:
        print("Invalid input, please try again!")
        continue  #To repeat the while loop if invalid input
#While loops ends here

#The second part of the app starts only if the user wanted to list results in a list.
#Here will be some operations with that list "list_results" which we already defined

print()
print("                            *************************                    ")
#Some funny operations with lists:
print()
print("Here is some useful information you might be interested in:")

#Find the maximum value in the list
print()
print("The maximum value in the list is:", max(list_results))

#Find the minimum value in the list:
print()
print("The minimum value in the list is:", min(list_results))

#Find the length of the list
print()
print("The list contains items:", len(list_results))

#Reverse the list and print it
print()
list_results.reverse()
print("Reversed list:", list_results)

#Reverse the list back
list_results.reverse()

#Find the sum of all numbers in the list
print()
print("The sum of numbers in the list is:", sum(list_results))

#Find the average number between num1 and num2
print()
print("The average number is:", sum(list_results) / len(list_results))

#Quit:
import time
print()
print("Thank you, Good bye !!!")
print("Quitting")
for i in range(5):
    print(".")
    time.sleep(0.2)
quit()
