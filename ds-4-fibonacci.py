"""
write a program to print the fibonnaci sequence up to given number.
"""

def fibonacciSeries() :
    try : num = int(input("Enter a number \n"))
    except : print("Invalid Input")
    else :
        start0 = 0
        start1 = 1

        while start1 < num :
            result = start0 + start1 # 0 + 1 = 1
            start0 = start1 # 1
            start1 = result # 1
            print("Fibonacci series:", result)
fibonacciSeries()