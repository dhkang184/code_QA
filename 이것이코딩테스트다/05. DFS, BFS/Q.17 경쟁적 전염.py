# https://www.acmicpc.net/problem/18405

from collections import deque
n, k = map(int, input().split())

data = []
virus = []

for i in range(n):
    data.append(list(map(int, input().split())))
    for j in range(n):
        if data[i][j] >0:
            virus.append((data[i][j], 0, i, j))

s,x,y = map(int, input().split())
virus.sort()

q = deque(virus)

dx = [-1,0,1,0]
dy = [0,1,0,-1]

while q:
    c_v, c_s, c_x, c_y = q.popleft()
    if s == c_s:
        break
    for i in range(4):
        nx = c_x + dx[i]
        ny = c_y + dy[i]

        if nx >=0 and nx < n and ny >=0 and ny<n:
            if data[nx][ny] ==0:
                data[nx][ny] = c_v
                q.append((c_v, c_s + 1, nx, ny))

print(data[x-1][y-1])