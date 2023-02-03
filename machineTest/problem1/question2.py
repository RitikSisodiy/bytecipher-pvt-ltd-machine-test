# python program to find a pair with the highest product from a given array
# of integers.
def max_product_pair(arr):
    n = len(arr)
    max_product = -float('inf') # minus infinity
    max_num1 = -float('inf')
    max_num2 = -float('inf')
    min_num1 = float('inf')
    min_num2 = float('inf')

    for i in range(n):
        # to find the two maximum mumbers
        if arr[i] > max_num1:
            max_num2 = max_num1
            max_num1 = arr[i]
        elif arr[i] > max_num2:
            max_num2 = arr[i]
        # to find the two minimun mumbers
        if arr[i] < min_num1:
            min_num2 = min_num1
            min_num1 = arr[i]
        elif arr[i] < min_num2:
            min_num2 = arr[i]
        # this will return maximum between given three
        max_product = max(max_product, max_num1 * max_num2, min_num1 * min_num2)
    
    return (min_num1, min_num2) if min_num1 * min_num2 > max_num1 * max_num2 else (max_num1, max_num2)
# test the funtion with given list
if __name__=="__main__":
    arr = [1, 2, 3, 4, 7, 0, 8, 4]
    print("Original array:", arr)
    result = max_product_pair(arr)
    print("Maximum product pair is:", result)

    arr = [0, -1, -2, -4, 5, 0, -6]
    print("\nOriginal array:", arr)
    result = max_product_pair(arr)
    print("Maximum product pair is:", result)
# Original array: [1, 2, 3, 4, 7, 0, 8, 4]
# Maximum product pair is: (8, 7)

# Original array: [0, -1, -2, -4, 5, 0, -6]
# Maximum product pair is: (-6, -4)