#https://www.acmicpc.net/problem/18405
# 21:00~ 21:22
from collections import deque

n, k =map(int, input().split())

data = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())

move_r = [0, 1, 0, -1] #동,남,서,북
move_c = [1,0,-1,0]
Q = deque()
Virus = []
for r in range(n):
    for c in range(n):
        if data[r][c] >0:
            Virus.append((data[r][c], r, c))
for v in sorted(Virus):
    Q.append(v)

while Q and s >0:
    step_len = len(Q)
    for s_idx in range(step_len):
        now_v, now_r, now_c = Q.popleft()
        for m_idx in range(4):
            next_r = now_r + move_r[m_idx]
            next_c = now_c + move_c[m_idx]
            if next_r >=0 and next_r <n and next_c >=0 and next_c<n:
                if data[next_r][next_c] ==0:
                    data[next_r][next_c] = now_v
                    Q.append((now_v, next_r, next_c))
    s -= 1

print(data[x-1][y-1])



