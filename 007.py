def isPrime(n):
    if (n == 1):
        return False
    elif (n == 2):
        return True
    else:
        for x in range(2,n):
            if(n % x == 0):
                return False
        return True


def primeAtIndex(index):
    counter = 1
    num = 3
    while counter != index:
        if isPrime(num):
            counter+=1
        num+=2
    return num-2