def sumBelow1000():
    sum = 0
    for num in range(0, 1000):
        if(num % 3 == 0 | num % 5 == 0):
            sum += num

    return sum

