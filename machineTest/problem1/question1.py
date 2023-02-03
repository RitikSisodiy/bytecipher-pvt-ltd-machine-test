# python program to find whether a given array of integers contains any
# duplicate element. Return true if any value appears at least twice in the said
# array and return false if every element is distinct.

def hasDuplicate(nums):
    checked = set()
    for num in nums:
        if num in checked:
            return True
        checked.add(num)
    return False

if __name__=="__main__":
    import random
    # genarating list of 100 elements with random number
    nums = [random.randint(1,200) for i in range(0,100)]
    # genarating list of 100 elements with unique number
    # nums = [i for i in range(0,100)]
    print(nums)
    if hasDuplicate(nums):
        print("list has dublicates")
    else:
        print("list has 0 dublicates")
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 
# 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
# list has 0 dublicates

# 185, 136, 80, 180, 49, 56, 91, 197, 154, 163, 122, 55, 17, 24, 100, 154, 42, 183, 19, 27, 158, 3, 136, 104, 87, 33, 80, 94, 195, 89, 106, 57, 96, 184, 152, 20, 84, 107, 110, 9, 11, 81, 62, 145, 152, 102, 194, 22, 110, 102, 92, 113, 93, 17, 198, 149, 87, 93, 179, 165, 113, 94, 2, 137, 194, 163, 82, 80, 163, 73, 83, 194, 124, 148, 97, 151, 21, 116, 188, 61, 195, 172, 73, 54, 17, 53, 44, 122, 73, 161, 198, 11, 106, 66, 78, 170, 45, 89, 53, 76]
# list has dublicates