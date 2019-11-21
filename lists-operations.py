a = int(input("please enter the 1st number: "))
b = int(input("please enter the 2nd number: "))
c = int(input("please enter the 3d number: "))
d = int(input("please enter the 4th number: "))
e = int(input("please enter the 5th number: "))
f = int(input("please enter the 6th number: "))
g = int(input("please enter the 7th number: "))
h = int(input("please enter the 8th number: "))
i = int(input("please enter the 9th number: "))
j = int(input("please enter the 10th number: "))
print()
list0 = [a, b, c, d, e, f, g, h, i, j]

print(list0)

print()

dd = str(input("if you want to find tha max value, enter mx, If you want to find the min value, enter mn: "))

if dd == "mn":
    print("the min value is: ", min(list0))
elif dd == "mx":
    print("The max value is: ", max(list0))
else:
    print("wrong value") ; quit()
print()

print("              **************************            ")

# example how to work with different list operations:
print()
print("how to find the index of an item")
print()

letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters)
print()

print("the index of 'r' is: ", letters.index('r'))
print("the index of 'p' is: ", letters.index('p'))

print()
print("find the max and min values within a list")

list1 = ['1', '2', '3', '4', '5', '6', '7', '8']
print(list1)
print("The max value is: ", max(list1))

print()
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list2)
print("The min value is: ", min(list1))

print()
print("remove 3 from the list2")
list2.remove(3)
print(list2)

print()
print("remove '4' from list1")
list1.remove('4')
print(list1)

print()
print("              ******************                ")
print()
print("Create a list from 1 - 10 with interval of 5")
print()
nums = list(range(0, 101, 5))
print(nums)

print()
print("                                  *************************             ")
print()
print("To find the how many items in the list we use the 'len' function")
print("the length of the list is: ", len(nums))

print()
print("               ****************************                             ")
print()
print("to revers the items in the list we use 'list.revers()' function")
nums.reverse()
print(nums)
