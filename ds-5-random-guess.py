"""
write a program using while loop to implement number a gussing game.
"""
import random

num = random.randint(0, 100)
def guess() :
    print("--------------------------------")
    try : userinput = int(input("Enter your input \n"))
    except: print("Invalid input")
    else :
        if userinput == num :
            print("You win !")
            exit()
        elif userinput > num :print("Your input is too large !")
        else : print("Your input is too small !")
while True : guess()