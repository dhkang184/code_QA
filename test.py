def test(N):
    answer =[]
    for i in range(2,10):
        result =""
        a = N
        while a//i >= 1:
            core = a%i
            a = a//i
            result = str(core) + result
            if a<i :
                result = str(a)+result
        print("%d: %s" %(i,result))
        k = list(map(int, result))
    return 0

print(test(33))