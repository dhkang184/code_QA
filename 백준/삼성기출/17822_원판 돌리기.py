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
            data[idx] = data[idx][-ki:] + data[idx][:(m-ki)]
        elif di == 1:
            data[idx] = data[idx][ki:] + data[idx][:ki]

    ext_data = [[INF]*(m+2) for _ in range(n)]
    for idx in range(n):
        ext_data[idx] =data[idx][-1:] + data[idx] + data[idx][:1]

    new_data = [[INF]*(m+2) for _ in range(n)]
    C = True #지울 값이 없는 경우
    total = 0
    cnt = 0
    for i in range(n):
        for j in range(m):
            if i == 0 :
                if ext_data[i][j+1] != ext_data[i][j+2] and ext_data[i][j+1] != ext_data[i][j] and ext_data[i][j+1] !=ext_data[i+1][j+1]:
                    new_data[i][j+1] = ext_data[i][j+1]
                    total += ext_data[i][j+1]
                    cnt +=1
                elif ext_data[i][j+1] != INF:
                    C = False
            elif i == n-1:
                if ext_data[i][j+1] != ext_data[i][j+2] and ext_data[i][j+1] != ext_data[i][j] and ext_data[i][j+1] !=ext_data[i-1][j+1]:
                    new_data[i][j+1] = ext_data[i][j+1]
                    total += ext_data[i][j + 1]
                    cnt += 1
                elif ext_data[i][j + 1] != INF:
                    C = False
            else:
                if ext_data[i][j+1] != ext_data[i][j+2] and ext_data[i][j+1] != ext_data[i][j] and ext_data[i][j+1] !=ext_data[i-1][j+1] and ext_data[i][j+1] !=ext_data[i+1][j+1]:
                    new_data[i][j+1] = ext_data[i][j+1]
                    total += ext_data[i][j + 1]
                    cnt += 1
                elif ext_data[i][j + 1] != INF:
                    C = False

    if C == True and cnt >0:
        avg = total/cnt
        for i in range(n):
            for j in range(m):
                if new_data[i][j+1] > avg and new_data[i][j+1] != INF:
                    new_data[i][j+1] -= 1
                elif new_data[i][j+1] < avg:
                    new_data[i][j+1] += 1

    data =[[0]*m for _ in range(n)]
    answer =0
    for i in range(n):
        for j in range(m):
            data[i][j] = new_data[i][j+1]
            if data[i][j] != INF:
                answer += data[i][j]


print(str(answer))