# https://www.acmicpc.net/problem/17837
# 시작시간: 23:50

n, k = map(int, input().split())

map_data = [list(map(int, input().split())) for _ in range(n)] #0: 흰색, 1: 빨강, 2: 파랑
move_data = [list(map(int, input().split())) for _ in range(k)]

c_data = [[False]*n for _ in range(n)]
for idx, x in enumerate(move_data):
    c_data[x[0]][x[1]] = [idx]
def move_case(data):
    move = [(0,1), (0,-1), (-1,0), (1,0)]
    x = data[0]
    y = data[1]
    m_case = data[2]
