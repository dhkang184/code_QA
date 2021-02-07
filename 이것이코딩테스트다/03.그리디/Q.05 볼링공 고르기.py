def solution():
    N,M = map(int, input().split())
    data = list(map(int, input().split()))
    result = 0
    array = [0] *11
    for x in data:
        array[x] += 1

    for y in array:
        N -= y
        result += N *y
    print(result)

solution()