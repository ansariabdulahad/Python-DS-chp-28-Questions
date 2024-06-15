"""
write a program that uses a while loop to convert a decimal to binary.
"""

def convertToBinary() :
    try : num = int(input("Enter a number to convert in bianry\n"))
    except: print("invalid input")
    else :
        b = ''
        while num > 0 :
            b = str(num % 2) + b
            num = num // 2
        print(b)
convertToBinary()