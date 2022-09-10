import numpy as np

def foo():
    print("")
    arr = np.arange(0,10)
    print(f"0. Default array \n{arr}\n")
    print(f"1. Add 10 to every value in array \n{arr+10}\n")
    print(f"2. Multiply every value in array by 5 \n{arr*10}\n")
    print(f"3. Send every value in array to the power of 3 \n{arr**3}\n")

    print(f"4. Get sum of all array values \n{np.add.reduce(arr)}\n")
    print(f"5. Get sum of all array values (with steps) \n{np.add.accumulate(arr)}\n")
    print(f"6. Create 0-9 multiplication table \n{np.multiply.outer(arr, arr)}\n")
    return

if __name__ == "__main__":
    foo()