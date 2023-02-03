# program to find missing numbers from a list
def find_missing_numbers(arr):
    n = len(arr)
    result = []
    for i in range(n-1):
        diff = arr[i+1] - arr[i]
        if diff > 1:
            for j in range(1, diff):
                result.append(arr[i] + j)
    return result
# test the funtion with 
if __name__=="__main__":
    import random
    n = 14
    arr = [i for i in range(0,n)] # for example
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    # deleting random numbers for list
    for i in range(0, random.randint(1,n-1)):del arr[random.randint(0,len(arr)-1)]
    # list before deletion
    print("given list \n",arr)
    #  [1, 2, 6, 7, 8, 9, 10, 11, 12, 13]
    print(find_missing_numbers(arr))