import time

def isPalindrome(num):
    if num[::-1] == num:
        return True
    else:
        return False

def solve():
    start = time.time()
    listOfPalindromes = []

    for i in range(100,1000):
        for j in range(100,1000):
            num = i * j
            if isPalindrome(str(num)):
                listOfPalindromes.append(num)

    #print(listOfPalindromes) --- Just for curiosity.
    print("Solution:",max(listOfPalindromes))
    end = time.time() - start
    print("Runtime:",end)