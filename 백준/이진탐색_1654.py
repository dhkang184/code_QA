#https://www.acmicpc.net/problem/1654
# 20:25~

k, n = map(int,input().split())

k_list = [int(input()) for _ in range(k)]

start = 1
end = max(k_list)
ans = 0
while start <= end:

    mid = (start+ end) //2
    num = 0
    for p in k_list:
        num += p//mid

    if num >=n:
        ans = max(ans, mid)
        start = mid +1
    else:
        end = mid -1

print(ans)