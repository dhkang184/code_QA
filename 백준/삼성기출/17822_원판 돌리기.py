# https://www.acmicpc.net/problem/17822
# 시작 시간: 19:35

n, m, t = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(n)]

m_data = [map(int, input().split()) for _ in range(t)]

INF = 1e9

for t_idx in range(t):
    xi, di, ki = m_data[t_idx]
    for idx in range(xi-1, n, xi):
        if di == 0:
            data[idx] = data[idx][-ki:] + data[idx][:-ki]
        elif di == 1:
            data[idx] = data[idx][ki:] + data[idx][:ki]

    new_data = [[INF]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if i == 0:
                if new_data[i][j] == new_data[i]
