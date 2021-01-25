#page 220

def solution():
    n = int(input())
    array = list(map(int, input().split()))
    d = [0]*100
    d[0] = array[0]
    d[1] = array[1]
    for x in range(2, n):
        d[x] = max(d[x-1], d[x-2]+array[x])

    print(d[n-1])