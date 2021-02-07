def solution():
    N = int(input())
    M = list(map(int, input().split()))
    M.sort()
    target = 1
    for x in M:
        if target < x:
            break
        target += x
    print(target)

solution()