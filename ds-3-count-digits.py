"""
write a program to count the number of digits in a given integer by user.
"""

def countDigits() :
    try : num = int(input("Enter your digits \n"))
    except : print("Invalid Input")
    else :
        length = 0
        while num > 0 :
            print(num)
            num = num // 10
            length = length + 1
        print("Length of digits:", length)
countDigits()