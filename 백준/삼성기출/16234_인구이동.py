#https://www.acmicpc.net/problem/16234
# 24:22~ 2:00 실패...
"""
from collections import deque

# 땅의 크기(N), L, R 값을 입력받기
n, l, r = map(int, input().split())

# 전체 나라의 정보(N x N)를 입력 받기
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 특정 위치에서 출발하여 모든 연합을 체크한 뒤에 데이터 갱신
def process(x, y, index):
    # (x, y)의 위치와 연결된 나라(연합) 정보를 담는 리스트
    united = []
    united.append((x, y))
    # 너비 우선 탐색 (BFS)을 위한 큐 라이브러리 사용
    q = deque()
    q.append((x, y))
    union[x][y] = index # 현재 연합의 번호 할당
    summary = graph[x][y] # 현재 연합의 전체 인구 수
    count = 1 # 현재 연합의 국가 수
    # 큐가 빌 때까지 반복(BFS)
    while q:
        x, y = q.popleft()
        # 현재 위치에서 4가지 방향을 확인하며
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 바로 옆에 있는 나라를 확인하여
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                # 옆에 있는 나라와 인구 차이가 L명 이상, R명 이하라면
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append((nx, ny))
                    # 연합에 추가하기
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    count += 1
                    united.append((nx, ny))
    # 연합 국가끼리 인구를 분배
    for i, j in united:
        graph[i][j] = summary // count

total_count = 0

# 더 이상 인구 이동을 할 수 없을 때까지 반복
while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1: # 해당 나라가 아직 처리되지 않았다면
                process(i, j, index)
                index += 1
    # 모든 인구 이동이 끝난 경우
    if index == n * n:
        break
    total_count += 1

# 인구 이동 횟수 출력
print(total_count)


"""

n, l, r = map(int, input().split())
# 이동 조건 : l <= 인구 차 <=r
M = [list(map(int, input().split())) for _ in range(n)]
move_r =[0, 1, 0, -1]
move_c =[1, 0, -1, 0]


def check_group(x, group_list):
    if x != group_list[x]:
        group_list[x] = check_group(group_list[x], group_list)
    return group_list[x]

def union_group(group_list, a,b):
    a = check_group(a, group_list)
    b = check_group(b, group_list)
    if a<b:
        group_list[b] = a
    else:
        group_list[a] =b

if n ==1:
    print(0)
else:
    count = 0
    while True:
        break_v = False
        same_v = False # 셀 값이 모두 같은지 체크
        group_list = [x for x in range(n * n)]  # r*n +c
        for _r in range(n):
            for _c in range(n):
                for x in range(4):
                    n_r = _r + move_r[x]
                    n_c = _c+move_c[x]
                    if n_r >= 0 and n_r <n and n_c >=0 and n_c <n:
                        if abs(M[_r][_c] - M[n_r][n_c]) >=l and abs(M[_r][_c] - M[n_r][n_c]) <= r:
                            break_v = True
                            union_group(group_list, _r * n + _c, n_r * n + n_c)
                        if abs(M[_r][_c] - M[n_r][n_c]) >0:
                            same_v = True
        if break_v == False or same_v == False:
            break
        else:
            count += 1
            group_V = [0]*(n*n)
            group_C = [0]*(n*n)
            for y_idx, y in enumerate(group_list):
                _c = y_idx%n
                _r = y_idx//n
                group_V[y] += M[_r][_c]
                group_C[y] +=1

            for z_idx, z in enumerate(group_list):
                _c = z_idx % n
                _r = z_idx // n
                M[_r][_c] = group_V[z] //group_C[z]

    print(count)
