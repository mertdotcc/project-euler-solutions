def difference100():
    sumOfTheSquares = 0
    squareOfTheSums = 0
    sums = 0

    for i in range(1,101):
        sums += i
        sumOfTheSquares += i**2

    squareOfTheSums = sums**2

    return squareOfTheSums - sumOfTheSquares