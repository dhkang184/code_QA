from collections import deque
def BFS(sang,fire):
    tmp_f = deque()
    tmp_s = deque()
    while sang:
        global cnt
        cnt += 1
        while fire:
            k = fire.popleft()
            if k[0] < M - 1:
                if board[k[0] + 1][k[1]] == '.':
                    board[k[0] + 1][k[1]] = '*'
                    tmp_f.append([k[0] + 1,k[1]])
            if k[0] > 0:
                if board[k[0] - 1][k[1]] == '.':
                    board[k[0] - 1][k[1]] = '*'
                    tmp_f.append([k[0] - 1,k[1]])
            if k[1] < N - 1:
                if board[k[0]][k[1] + 1] == '.':
                    board[k[0]][k[1] + 1] = '*'
                    tmp_f.append([k[0],k[1] + 1])
            if k[1] > 0:
                if board[k[0]][k[1] - 1] == '.':
                    board[k[0]][k[1] - 1] = '*'
                    tmp_f.append([k[0],k[1] - 1])
        while sang:
            k = sang.popleft()
            if k[0] == 0 or k[0] == M-1 or k[1] == 0 or k[1] == N-1:
                print(cnt)
                return
            if board[k[0] + 1][k[1]] == '.':
                board[k[0] + 1][k[1]] = '@'
                tmp_s.append([k[0] + 1, k[1]])
            if board[k[0] - 1][k[1]] == '.':
                board[k[0] - 1][k[1]] = '@'
                tmp_s.append([k[0] - 1, k[1]])
            if board[k[0]][k[1] + 1] == '.':
                board[k[0]][k[1] + 1] = '@'
                tmp_s.append([k[0], k[1] + 1])
            if board[k[0]][k[1] - 1] == '.':
                board[k[0]][k[1] - 1] = '@'
                tmp_s.append([k[0], k[1] - 1])
        sang = tmp_s
        # print(sang)
        fire = tmp_f
        tmp_f = deque()
        tmp_s = deque()
        # print(board)
    print('IMPOSSIBLE')
for _ in range(int(input())):
    cnt = 0
    N, M = map(int,input().split())
    board = [list(map(str, input())) for _ in range(M)]
    sang = deque()
    fire = deque()

    for i in range(M):
        for j in range(N):
            if board[i][j] == '@':
                sang.append([i,j])
            elif board[i][j] == '*':
                fire.append([i,j])
    BFS(sang, fire)

# from collections import deque
# T = int(input())
#
#
# def BFS(user_q,fire_q):
#     cnt = 0
#     dx = [1, 0, -1, 0]
#     dy = [0, 1, 0, -1]
#     while user_q:
#         cnt += 1
#         user_nq = deque()
#         fire_nq = deque()
#         while fire_q:
#             c_fire = fire_q.popleft()
#             fire_h = c_fire[0]
#             fire_w = c_fire[1]
#             # if fire_h == 0 or fire_w ==0 or fire_h == H or fire_w == W:
#             #    return cnt
#             for mx, my in zip(dx, dy):
#                 next_w = fire_w + mx
#                 next_h = fire_h + my
#                 if test_map[next_h][next_w] == '.' and next_w > -1 and next_w < W and next_h > -1 and next_h < H:
#                     test_map[next_h][next_w] = '*'
#                     fire_nq.append([next_h, next_w])
#                 elif test_map[next_h][next_w] == '@' and next_w > -1 and next_w < W and next_h > -1 and next_h < H:
#                     test_map[next_h][next_w] = '*'
#                     fire_nq.append([next_h, next_w])
#         while user_q:
#             c_user = user_q.popleft()
#             user_h = c_user[0]
#             user_w = c_user[1]
#             if user_h == 0 or user_h == H - 1 or user_w == 0 or user_w == W - 1:
#                 return print(cnt)
#             for mx, my in zip(dx, dy):
#                 next_w = user_w + mx
#                 next_h = user_h + my
#                 if test_map[next_h][next_w] == '.' and next_w > -1 and next_w < W and next_h > -1 and next_h < H:
#                     user_nq.append([next_h, next_w])
#                     test_map[next_h][next_w] = '@'
#
#         user_q = user_nq
#         fire_q = fire_nq
#     return print("IMPOSSIBLE")
#
# for _ in range(T):
#     W, H = map(int, input().split())
#     test_map = [list(map(str, input())) for x in range(H)]
#     # test_map = []
#     # for x in range(H):
#     #     test_map.append(list(map(str, input())))
#     user_q = deque()
#     fire_q = deque()
#     for h in range(H):
#         for w in range(W):
#             if test_map[h][w] == '@':
#                 user_q.append([h,w])
#                 test_map[h][w] = '.'
#             elif test_map[h][w] == '*':
#                 fire_q.append([h,w])
#     BFS(user_q, fire_q)