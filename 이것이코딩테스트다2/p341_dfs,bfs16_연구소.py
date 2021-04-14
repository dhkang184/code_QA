#https://www.acmicpc.net/problem/14502
# 18:55 ~ 19:40

from collections import deque
from itertools import combinations

n, m = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(n)]
virus = []
zero_list = []
move_r =[0, 1, 0, -1] #동, 남, 서, 북
move_c =[1, 0, -1, 0]
count = 0
answer = -1
def Virus(data, virus, count):
    N_map = [[0] * len(data[0]) for _ in range(len(data))]
    for r in range(len(data)):
        for c in range(len(data[0])):
            N_map[r][c] = data[r][c]
    Q = deque(virus)

    while Q:
        now_r, now_c = Q.popleft()
        for m_idx in range(4):
            next_r = now_r + move_r[m_idx]
            next_c = now_c + move_c[m_idx]
            if next_r>=0 and next_r < n and next_c>=0 and next_c <m:
                if N_map[next_r][next_c] ==0:
                    N_map[next_r][next_c] = 2
                    Q.append([next_r,next_c])
                    count -=1
    return count

for r in range(n):
    for c in range(m):
        if data[r][c] == 2:
            virus.append([r,c])
        elif data[r][c] == 0:
            zero_list.append([r,c])
            count +=1

wall_list = list(combinations(zero_list, 3))
for wall in wall_list:
    for n_wall in wall:
        data[n_wall[0]][n_wall[1]] = 1

    answer = max(answer, Virus(data, virus, count-3))
    for n_wall in wall:
        data[n_wall[0]][n_wall[1]] = 0

print(answer)




