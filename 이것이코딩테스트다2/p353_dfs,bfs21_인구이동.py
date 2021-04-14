#https://www.acmicpc.net/problem/16234
# 23:25~ 00:20
"""
n,L,R = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(n)]

answer = 0

from collections import deque
import heapq


while True:
    check_map = [[False]*n for a in range(n)] # 한번 그룹 처리하면 True
    group_num = 0
    move_r = [0,1,0,-1]
    move_c = [1,0,-1,0]
    end_config = True

    Q = deque()

    for r in range(n):
        for c in range(n):
            if check_map[r][c] == False:
                check_map[r][c] = True
                Q.append((r,c))
                group_list =[(r,c)]
                while Q:
                    now_r, now_c = Q.popleft()
                    sum_num = data[now_r][now_c]
                    sum_len = 1
                    for m_idx in range(4):
                        next_r = now_r + move_r[m_idx]
                        next_c = now_c + move_c[m_idx]
                        if next_r>=0 and next_r<n and next_c >=0 and next_c<n:
                            if check_map[next_r][next_c] == False and abs(data[now_r][now_c] - data[next_r][next_c]) >=L and abs(data[now_r][now_c] - data[next_r][next_c]) <=R:
                                Q.append((next_r, next_c))
                                group_list.append((next_r,next_c))
                                check_map[next_r][next_c] = True
                                end_config = False
                                sum_num += data[next_r][next_c]
                                sum_len +=1
                avg_num = sum_num//sum_len
                for n_r, n_c in group_list:
                    data[n_r][n_c] =avg_num

    if end_config == True:
        break
    else:
        answer +=1

print(answer)
"""

from collections import deque

N, L, R = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]


def check_union(sr, sc, visited):
    union = []
    q = deque([(sr, sc)])
    visited[sr][sc] = True
    union.append((sr, sc))

    while q:
        r, c = q.popleft()
        for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < N:
                if L <= abs(board[r][c] - board[nr][nc]) <= R and not visited[nr][nc]:
                    visited[nr][nc] = True
                    union.append((nr, nc))
                    q.append((nr, nc))
    # print(union)
    return union

def move_pop(unions):
    population = 0
    for u in unions:
        for c in u:
            population += board[c[0]][c[1]]
        population = population // len(u)
        for c in u:
            board[c[0]][c[1]] = population
        population = 0


def diff_n(y, x):
    for i in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        ny, nx = y + i[0], x + i[1]
        if 0 <= ny < N and 0 <= nx < N:
            if L <= abs(board[y][x] - board[ny][nx]) <= R:
                return True
    return False


def solution():
    cnt = 0

    while True:
        unions = []
        visited = [[False for _ in range(N)] for _ in range(N)]
        flag = False

        for i in range(N):
            for j in range(N):
                if not visited[i][j] and diff_n(i, j):
                    tmp = check_union(i, j, visited)
                    unions.append(tmp)
                    flag = True
        if flag:
            move_pop(unions)
            cnt += 1

        else:
            return cnt

print(solution())