def multiple(num):
    sum = 0
    for i in range(1,num):
        if (i%3 == 0 and i%5 == 0):
            sum += i
    print(sum)

multiple(100)