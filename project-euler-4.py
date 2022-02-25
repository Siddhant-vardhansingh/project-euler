def ispalindrome(num):
    a = str(num)
    b = a[::-1]
    if (a == b):
        return True
def palindrome_product(num):
    a = "1"+"0"*(num-1)
    b = "9"*num
    c = int(a)
    d = int(b)
    list = []
    for i in range(c, d+1):
        for j in range(c,d+1):
            e = i*j
            if(ispalindrome(e)):
                list.append(e)
    list.sort()
    value = list.pop()
    print(value) 

palindrome_product(4)