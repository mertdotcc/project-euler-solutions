import time

def minPrimeFactor(n):
    assert n >= 2
    for num in range(2, (int(n**0.5) + 1)):
        if n % num == 0:
            return num
    return n

def solve(n):
    start = time.time()
    while True:
        minimumPrimeFactor = minPrimeFactor(n)
        if minimumPrimeFactor < n:
            n = n / minimumPrimeFactor
        else:
            print("Solution:",n)
            end = time.time() - start
            print("Runtime:",end)
            return
