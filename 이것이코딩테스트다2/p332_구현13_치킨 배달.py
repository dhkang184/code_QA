#https://www.acmicpc.net/problem/15686
# 00:50~

n,m = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(n)]

house = []
chichen = []

for r in range(n):
    for c in range(n):
        if data[r][c] == 1:
            house.append((r,c))
        elif data[r][c] ==2:
            chichen.append((r,c))

from itertools import combinations

chichen_list = list(combinations(chichen, m))

answer = 1e9

for x in chichen_list:
    n_sum =0
    for h in house:
        dis = 10e9
        for ch in x:
            dis = min(dis, abs(ch[0] - h[0])+ abs(ch[1] - h[1]))
        n_sum += dis
    answer = min(answer, n_sum)

print(answer)