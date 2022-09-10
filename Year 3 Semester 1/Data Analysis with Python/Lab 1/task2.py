import numpy as np

def foo():
    print("")
    arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f"1.0. Default 2D array \n{arr2d}\n")
    print(f"1.1. Regular indexing \n{arr2d[0]}, {arr2d[1][1]}\n")
    print(f"1.2. Negative indexing (reversed order) \n{arr2d[-1]}, {arr2d[0][-0]}\n")   # -0 == 0
    
    arr1d = np.arange(0,10)
    print(f"2.0. Default 1D array \n{arr1d}\n")
    print(f"2.1. Slicing array with [from:to:step] (excluding 'to') \n{arr1d[2:7:2]}\n")
    print(f"2.2. Slice hack for easy array revesion \n{arr1d[::-1]}\n")
    print(f"2.3. Slicing last elements from subarrays in 2D array \n{arr2d[::, 1::-1]}\n")
    return

if __name__ == "__main__":
    foo()