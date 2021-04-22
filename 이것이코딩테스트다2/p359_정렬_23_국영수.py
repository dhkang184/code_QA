#https://www.acmicpc.net/problem/10825
# 23:25~ 23:40

n = int(input())

data = []
for _ in range(n):
    name, ko, en, ma = list(map(str, input().split()))
    data.append((name, int(ko), int(en), int(ma)))

new_data = sorted(data, key=lambda x: (-x[1], x[2], -x[3], x[0]))

for x in new_data:
    print(x[0])
