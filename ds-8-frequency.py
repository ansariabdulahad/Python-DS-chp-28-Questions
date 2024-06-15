"""
write a program that uses a while loop to find the frequencyof each element in a given list.
"""

def frequency() :
    nums = [1, 1, 1, 1, 12, 33, 4, 5, 6, 47, 8, 9, 1, 4, 5, 6, 77, 8, 9, 1, 12, 3, 44, 5, 6, 77]
    i = 0
    counter = {}

    while i < len(nums) :
        num = nums[i]
        if num in counter :
            counter[num] = counter[num] + 1
        else :
            counter[num] = 1
        i = i + 1

    for key in counter:
        print(f"{key} if {counter[key]} times present")
frequency()