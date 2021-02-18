# https://www.acmicpc.net/problem/14501

n = int(input())

T = []
P =[]
dp = [0] * (n+1)
for x in range(n):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
max_value = 0
for i in range(n-1, -1, -1):
    time = T[i] +i
    if time <=n:
        dp[i] = max(P[i] + dp[time], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value
print(max_value)

