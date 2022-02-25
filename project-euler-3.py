def largest_prime(num):
    list = []
    list2 = []
    list3 = []
    for i in range(1,num+1):
        if(num%i == 0):
            list.append(i)
    for j in list:
        for k in range(1,j+1):
            if(j%k == 0):
                list2.append(k)
                if (list2 == [1,j]):
                    list3.append(j)
        list2 = []

    value = list3.pop()
    print(value)

largest_prime(13195)