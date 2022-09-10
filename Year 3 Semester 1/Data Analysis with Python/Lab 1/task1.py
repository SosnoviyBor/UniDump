import numpy as np

def foo():
    print("\n   [D] stads for 'Determined'\n   [R] stands for 'Random'\n")   # For visibility
    arr = np.arange(0,1,0.1)
    print(f"1. [D] An array that ranges from 0 to 1 (excluding last) with step 0.1\n{arr}\n")

    arr = np.ones([2,4], dtype=int)
    print(f"2. [D] An array of 1s, epic\n{arr}\n")

    arr = np.zeros([2,4], dtype=int)
    print(f"3. [D] Same as previous, but for zeros\n{arr}\n")

    arr = np.linspace(3,1,4)
    print(f"4. [D] An array of evenly destributed 4 floats between 3 and 1\n{arr}\n")

    arr = np.random.random([2,4])
    print(f"5. [R] 2x4 array of random floats between 0 and 1\n{arr}\n")

    arr = np.random.randint(1,50,[2,4])
    print(f"6. [R] 2x4 array of random ints between 1 and 50 (excluding last)\n{arr}\n")

    arr = np.empty(10)
    print(f"7. [D/R] Semi-random array of 10 elements. Only reads data on call \n{arr}\n")
    return

if __name__ == "__main__":
    foo()