import math
import time

def isPrime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False

def sumOfPrimesUnder(num):
    sum = 0
    start = time.time()
    for i in range(2,num):
        if isPrime(i):
            sum += i
    print("Sum:", sum)
    end = time.time() - start
    print("Runtime:", end)
