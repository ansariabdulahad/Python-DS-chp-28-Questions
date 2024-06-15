"""
write a python program to find the factorial of given user input.
"""

def factorialNumber() :
    try : num = int(input("Enter a number\n"))
    except: print("Invalid input")
    else :
        factorial = 1
        """for index in range(num, 0, -1) :
            factorial = factorial * index
        print(f"Factorial of a number {num} is {factorial}")"""

        # using while loop
        while num > 0 :
            factorial = factorial * num
            num = num - 1
        print(f"Factorial of a number is {factorial}")
factorialNumber()