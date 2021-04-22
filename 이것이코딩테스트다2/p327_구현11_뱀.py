#https://www.acmicpc.net/problem/3190

# 22:55~ 23:55

from collections import deque

n = int(input())
M = [[0]*n for _ in range(n)]
k = int(input())
for _ in range(k):
    r, c = map(int, input().split())
    M[r-1][c-1] = 9
l = int(input())
l_list = [(input().split()) for _ in range(l)]

move_row = [0, 1, 0, -1] #우, 하, 좌, 상
move_col = [1, 0, -1, 0]
move_l = {0: 3, 1: 0, 2: 1, 3: 2}
move_d = {0: 1, 1: 2, 2: 3, 3: 0}
direction = 0

Q = [(0,0)]
count = 0
while True:
    count += 1
    now_r, now_c = Q[0]
    new_r = now_r + move_row[direction]
    new_c = now_c + move_col[direction]
    if new_r >= 0 and new_r < n and new_c >=0 and new_c <n and (new_r, new_c) not in Q:
        if M[new_r][new_c] == 9:
            Q = [(new_r, new_c)] + Q
            M[new_r][new_c] =0
        else:
            Q = [(new_r, new_c)] + Q[:-1]
        if l_list:
            if l_list[0][0] == str(count) and l_list[0][1] == "D":
                direction = move_d[direction]
                l_list.pop(0)
            elif l_list[0][0] == str(count) and l_list[0][1] == "L":
                direction = move_l[direction]
                l_list.pop(0)
    else:
        break

print(count)
