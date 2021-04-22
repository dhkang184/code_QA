#https://programmers.co.kr/learn/courses/30/lessons/60063

# 22:20~ 23:00

def solution(board):
    answer = 0
    n = len(board)
    visited_1 = [[False]*n for _ in range(n)] #가로
    visited_2 = [[False] * n for _ in range(n)] #세로
    move_r = [0,1,0,-1]
    move_c = [1,0,-1,0]

    from collections import deque
    Q = deque()
    Q.append(((0,0,0,0,1)))
    while True:
        step, r1, c1, r2, c2 = Q.popleft()
        if (r1,c1) == (n-1, n-1) or (r2,c2) == (n-1, n-1):
            return step
        if r1 == r2: #가로
            for mr, mc in zip(move_r, move_c):
                next_r1 = r1 +mr
                next_c1 = c1+ mc
                next_r2 = r2 +mr
                next_c2 = c2 +mc
                if 0<=next_r1 <n and 0<=next_c1 <n and 0<=next_r2 <n and 0<=next_c2 <n:
                    if visited_1[min(next_r1, next_r2)][min(next_c1, next_c2)] == False and board[next_r1][next_c1] ==0 and board[next_r2][next_c2] ==0:
                        Q.append((step +1, next_r1, next_c1, next_r2, next_c2))
                        visited_1[min(next_r1, next_r2)][min(next_c1, next_c2)] = True
            next_r1 = r1
            next_c1 = c1
            next_r2 = r1 +1
            next_c2 = c1
            if 0 <= next_r1 < n and 0 <= next_c1 < n and 0 <= next_r2 < n and 0 <= next_c2 < n:
                if visited_2[min(next_r1, next_r2)][min(next_c1, next_c2)] == False and board[next_r1][next_c1] == 0 and \
                        board[next_r2][next_c2] == 0 and board[r2+1][c2] ==0:
                    Q.append((step + 1, next_r1, next_c1, next_r2, next_c2))
                    visited_2[min(next_r1, next_r2)][min(next_c1, next_c2)] = True

            next_r1 = r1
            next_c1 = c1
            next_r2 = r1 -1
            next_c2 = c1
            if 0 <= next_r1 < n and 0 <= next_c1 < n and 0 <= next_r2 < n and 0 <= next_c2 < n:
                if visited_2[min(next_r1, next_r2)][min(next_c1, next_c2)] == False and board[next_r1][next_c1] == 0 and \
                        board[next_r2][next_c2] == 0 and board[r2 -1][c2] ==0:
                    Q.append((step + 1, next_r1, next_c1, next_r2, next_c2))
                    visited_2[min(next_r1, next_r2)][min(next_c1, next_c2)] = True

            next_r1 = r2 +1
            next_c1 = c2
            next_r2 = r2
            next_c2 = c2
            if 0 <= next_r1 < n and 0 <= next_c1 < n and 0 <= next_r2 < n and 0 <= next_c2 < n:
                if visited_2[min(next_r1, next_r2)][min(next_c1, next_c2)] == False and board[next_r1][next_c1] == 0 and \
                        board[next_r2][next_c2] == 0 and board[r1 + 1][c1] == 0:
                    Q.append((step + 1, next_r1, next_c1, next_r2, next_c2))
                    visited_2[min(next_r1, next_r2)][min(next_c1, next_c2)] = True

            next_r1 = r2 -1
            next_c1 = c2
            next_r2 = r2
            next_c2 = c2
            if 0 <= next_r1 < n and 0 <= next_c1 < n and 0 <= next_r2 < n and 0 <= next_c2 < n:
                if visited_2[min(next_r1, next_r2)][min(next_c1, next_c2)] == False and board[next_r1][next_c1] == 0 and \
                        board[next_r2][next_c2] == 0 and board[r1 - 1][c1] == 0:
                    Q.append((step + 1, next_r1, next_c1, next_r2, next_c2))
                    visited_2[min(next_r1, next_r2)][min(next_c1, next_c2)] = True

        else:  # 가로
            for mr, mc in zip(move_r, move_c):
                next_r1 = r1 + mr
                next_c1 = c1 + mc
                next_r2 = r2 + mr
                next_c2 = c2 + mc
                if 0 <= next_r1 < n and 0 <= next_c1 < n and 0 <= next_r2 < n and 0 <= next_c2 < n:
                    if visited_2[min(next_r1, next_r2)][min(next_c1, next_c2)] == False and board[next_r1][
                        next_c1] == 0 and board[next_r2][next_c2] == 0:
                        Q.append((step + 1, next_r1, next_c1, next_r2, next_c2))
                        visited_2[min(next_r1, next_r2)][min(next_c1, next_c2)] = True
            next_r1 = r1
            next_c1 = c1
            next_r2 = r1
            next_c2 = c1 +1
            if 0 <= next_r1 < n and 0 <= next_c1 < n and 0 <= next_r2 < n and 0 <= next_c2 < n:
                if visited_1[min(next_r1, next_r2)][min(next_c1, next_c2)] == False and board[next_r1][next_c1] == 0 and \
                        board[next_r2][next_c2] == 0 and board[r2][c2+1] == 0:
                    Q.append((step + 1, next_r1, next_c1, next_r2, next_c2))
                    visited_1[min(next_r1, next_r2)][min(next_c1, next_c2)] = True

            next_r1 = r1
            next_c1 = c1
            next_r2 = r1
            next_c2 = c1 - 1
            if 0 <= next_r1 < n and 0 <= next_c1 < n and 0 <= next_r2 < n and 0 <= next_c2 < n:
                if visited_1[min(next_r1, next_r2)][min(next_c1, next_c2)] == False and board[next_r1][next_c1] == 0 and \
                        board[next_r2][next_c2] == 0 and board[r2][c2 - 1] == 0:
                    Q.append((step + 1, next_r1, next_c1, next_r2, next_c2))
                    visited_1[min(next_r1, next_r2)][min(next_c1, next_c2)] = True

            next_r1 = r2
            next_c1 = c2 +1
            next_r2 = r2
            next_c2 = c2
            if 0 <= next_r1 < n and 0 <= next_c1 < n and 0 <= next_r2 < n and 0 <= next_c2 < n:
                if visited_1[min(next_r1, next_r2)][min(next_c1, next_c2)] == False and board[next_r1][next_c1] == 0 and \
                        board[next_r2][next_c2] == 0 and board[r1][c1 + 1] == 0:
                    Q.append((step + 1, next_r1, next_c1, next_r2, next_c2))
                    visited_1[min(next_r1, next_r2)][min(next_c1, next_c2)] = True
            next_r1 = r2
            next_c1 = c2 - 1
            next_r2 = r2
            next_c2 = c2
            if 0 <= next_r1 < n and 0 <= next_c1 < n and 0 <= next_r2 < n and 0 <= next_c2 < n:
                if visited_1[min(next_r1, next_r2)][min(next_c1, next_c2)] == False and board[next_r1][next_c1] == 0 and \
                        board[next_r2][next_c2] == 0 and board[r1][c1 - 1] == 0:
                    Q.append((step + 1, next_r1, next_c1, next_r2, next_c2))
                    visited_1[min(next_r1, next_r2)][min(next_c1, next_c2)] = True

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))