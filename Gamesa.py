import random
import math
import time

choice = 0
##############################################################################
input("Murder case \nPress Enter to continue")

input("\033[91m. . .\nOnce upon the time...\033[0m")
##############################################################################
choice = int(input("\033[91mgrrrrr he said \n1 - kill\n0 - save\n \033[0m"))
if choice == 1:
    time.sleep(2)
    input("kill")
    choice = 0
    print (choice)
elif choice == 0:
    input("save")
    print(choice)





