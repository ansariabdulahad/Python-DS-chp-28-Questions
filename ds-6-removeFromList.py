"""
write a program  that uses while loop to remove all occurences of a given element from a list.
"""

def removeFromList() :
    nums = [12, 3, 34, 4351, 212, 34, 12, 3, 1, 5,62, 2, 3, 3]
    i = 0
    try : userInput = int(input("Enter your number\n"))
    except: print("Invalid input")
    else :
        # print(nums)
        print('--------------------------------', len(nums))
        while i < len(nums) :
            num = nums[i]
            if num == userInput : nums.pop(i)
            i = i + 1
        print("After pop list is ", nums)
removeFromList()