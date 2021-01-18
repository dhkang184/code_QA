#page 99

def solution1():
    result = 0
    n,k = map(int, input().split())

    while n >= k:
        while n%k !=0:
            n -=1
            result +=1
        n //=k
        result +=1
    while n> 1:
        n -= 1
        result +=1
    print("SOLUTION1: %d" %result)

def solution2():
    result = 0
    n,k = map(int, input().split())
    while n >=k:
        target = (n//k) *k
        result += n - target
        n = target//k
        result += 1
    result += (n-1)
    print("SOLUTION2: %d" %result)
solution1()
solution2()

