# https://www.acmicpc.net/problem/18353
import sys

n = int(input())
#D = list(sys.stdin.readline().rstrip().split())
D = list(map(int,input().split()))

data = D[::-1]
dp = [1]*n
for i in range(1, n):
    for j in range(0,i):
        if data[j] < data[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(n - max(dp))