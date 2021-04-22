#https://www.acmicpc.net/problem/18310
# 23:45~24:00
"""
n = int(input())
data = list(map(int, input().split()))
ans_idx = 1e9
ans_sum = 1e9

for d_idx in data:
    n_idx = d_idx
    n_sum = 0
    for D in data:
        n_sum += abs(D-d_idx)

    if ans_sum > n_sum:
        ans_sum = n_sum
        ans_idx = d_idx
print(ans_idx)
"""

n = int(input())

data = list(map(int, input().split()))

data.sort()
print(data[(n-1)//2])