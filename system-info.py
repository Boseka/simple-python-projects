#Python3 script to print out some useful linus system information, by Boseka !!!
G = '\033[32m'
R = '\033[31m'
W = '\033[m'
Y = '\033[33m'
HG = '\033[42m'

import platform
from time import sleep

print(Y, "Some information about the system \nThis should work on linux systems, I have no idea if you can run this on Windows", W)
print(R, "Do you want the tool to display some system information, \nsome information might be sensitive? (yes/no)", W)
user_input = input("")
print()
if user_input == "no":
    print(R ,"quitting .......", W)
    for i in range(5):
        print(R, '.', W)
        sleep(0.1)
    quit()
else:
    print(G, "System:", platform.system())
    print("Machine:", platform.machine())
    print("Platform:", platform.platform())
    print("Version:", platform.version())
    print("Python version:", platform.python_version())
    print("Architecture:", platform.architecture())
    print("Release:", platform.release())
    print("Linux distribution:", platform.linux_distribution())
    print("Processor:", platform.processor())
    print("Python compiler:", platform.python_compiler())
    print("Host:", platform.node())
    print("Python build:", platform.python_build())
    print()
    print("Summary:\n", platform.uname(), W)

import time
print()
print(Y, "Thank you, Good bye !!!")
print("Quitting")
for i in range(5):
    print(".")
    time.sleep(0.1)
print()
quit()
