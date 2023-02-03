#program to fine square root if given number using recursion 
def square_root(number ,precision=0.001 , root=1):
    if number<0:
        print("Negative numbers doesn't have real square roots since a square is either positive or 0.")
        return
    if abs(root * root - number) > precision:
        root = 0.5 * (root + number / root)
        return square_root(number,precision,root)
    else:
        return round(root,6)
# test the funtion with 
if __name__=="__main__":
    n = 4
    print(f"squre root of {n}:")
    print(square_root(n))