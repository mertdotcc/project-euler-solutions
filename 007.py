import math
import time

def isPrime(number):
    if(number > 1):
        if(number == 2):
            return True
        if(number % 2 == 0):
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if(number % current == 0):
                return False
        return True
    return False

def primeAtIndex(index):
    start = time.time()
    if(index == 1):
        num = 2
        print("Result:", 2)
        end = time.time() - start
        print("Runtime:", end)
    else:
        counter = 1
        num = 3
        while counter != index:
            if isPrime(num):
                counter+=1
            num+=2
        print("Result:", num-2)
        end = time.time() - start
        print("Runtime:", end)
