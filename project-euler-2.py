def even_fibonacci(num):
    a = 1
    b = 2
    c = 0
    sum = 0
    list = [2]
    for i in range(4000000):
        c = a + b
        if (c%2 == 0):
            list.append(c)
        a = b
        b = c
        if (c>=num):
            break
    for j in list:
        sum += j
    print(sum)

even_fibonacci(1000)