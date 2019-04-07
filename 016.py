import time

def solve():
    start = time.time()
    num = 2**1000
    s = sum(int(n) for n in str(num))
    print("Solution:", s)
    end = time.time() - start
    print("Runtime:", end)
