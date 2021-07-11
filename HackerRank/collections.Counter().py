#https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

X = int(input())
items = list(map(int, input().split()))
N = int(input())
items_c = Counter(items)
ans = 0
for n in range(N):
    size , price = map(int, input().split())
    if items_c[size] >0:
        items_c[size] -= 1
        ans += price

print(ans)