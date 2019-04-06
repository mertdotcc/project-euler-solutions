import math
import time

def solve():
    start = time.time()
    num = math.factorial(100)
    digitsSum = sum(int(n) for n in str(num))
    print("Solution:",digitsSum)
    end = time.time() - start
    print("Runtime:",end)