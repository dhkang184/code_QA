#피보나치 함수 소스코드(기본 로직)
def fibo(x):
    if x == 1 or x==2:
        return 1
    return fibo(x -1)+ fibo(x-2)

#피보나치 수열 소스코드(재귀), Memoization
d =[0]*100 # memoization을 위한 초기 리스트 생성

def fibo2(x):
    if x == 1 or x ==2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo2(x-1)+fibo2(x-2)
    return d[x]

print(fibo2(10))