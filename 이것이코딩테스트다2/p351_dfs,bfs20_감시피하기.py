#https://www.acmicpc.net/problem/18428
#22:45~ 23:15

from itertools import combinations
n = int(input())

data = [list(map(str, input().split())) for _ in range(n)]

T_list = []
X_list = []
S_list = []
for r in range(n):
    for c in range(n):
        if data[r][c] == "X":
            X_list.append((r,c))
        elif data[r][c] == "T":
            T_list.append((r,c))
        elif data[r][c] == "S":
            S_list.append((r,c))

Wall_list = list(combinations(X_list, 3))

def Check_f(Wall):
    new_map =[["X"]* n for _ in range(n)]
    move_r = [0,1,0,-1]
    move_c = [1,0,-1,0]
    S_config = True  # 학생 찾으면 False
    for r,c in S_list:
        new_map[r][c] = "S"

    for r,c in T_list:
        new_map[r][c] = "T"

    for r,c in Wall:
        new_map[r][c] = "O"

    for r,c in T_list:
        for m_idx in range(4):
            next_r = r+move_r[m_idx]
            next_c = c+move_c[m_idx]

            while next_c>=0 and next_c <n and next_r >=0 and next_r<n:
                if new_map[next_r][next_c] == "S":
                    S_config = False
                    return S_config
                elif new_map[next_r][next_c] == "O":
                    break
                next_r += move_r[m_idx]
                next_c += move_c[m_idx]
    return S_config

ans_config = False
for W in Wall_list:
    if Check_f(W):
        ans_config = True
        break
if ans_config:
    print("YES")
else:
    print("NO")