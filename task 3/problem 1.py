def oddsum():
    list = [3, 2, 4, 6, 5, 7, 8, 0, 1]

    thesum = 0
    for i in list:
        if -100 <= i <= 100:
            if i % 2 != 0:
                thesum += i

    return thesum

result = oddsum()
print(result)
#wrote all the code for code area task in hackerrank itself except this one
