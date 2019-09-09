# 2018 카카오 : https://www.welcomekakao.com/learn/courses/30

# https://www.welcomekakao.com/learn/courses/30/lessons/42894

"""
파이썬 2차원 배열 만들기
w, h = 8, 5.
Matrix = [[0 for x in range(w)] for y in range(h)]

"""
"""
인터넷 솔루션...
def solution(board):
    total_col = len(board[0])
    total_row = len(board)
    answer = 0
    pre_answer = -1
    count = 0
    black_blocks = []
    while(count <= 2) :


        # Set black blocks
        count += 1
        for col in range(total_col) :
            idx = 0

            while(True) :

                if board[0][col] != 0:
                    break

                if idx >= total_row - 1:
                    board[idx][col] = -1
                    black_blocks.append([idx, col])
                    break

                if board[idx + 1][col] != 0 :
                    board[idx][col] = -1
                    black_blocks.append([idx, col])
                    break

                idx += 1



        # 2 x 3 block (height x width)
        for row in range(total_row - 1) :
            for col in range(total_col - 2) :
                block_info = []
                if board[row][col] != 0 :
                    block_info.append(board[row][col])
                    block_info.append(board[row][col + 1])
                    block_info.append(board[row][col + 2])
                    block_info.append(board[row + 1][col])
                    block_info.append(board[row + 1][col + 1])
                    block_info.append(board[row + 1][col + 2])

                block_Set = set(block_info)

                if block_info.count(-1) == 2 and block_info.count(0) == 0 and len(block_Set) == 2:
                    answer += 1
                    board[row][col] = 0
                    board[row][col + 1] = 0
                    board[row][col + 2] = 0
                    board[row + 1][col] = 0
                    board[row + 1][col + 1] = 0
                    board[row + 1][col + 2] = 0

                    for idx in black_blocks :
                        x, y = idx
                        board[x][y] = 0
                    black_blocks = []
                    count = 0
        # 3 x 2 block (height x width)
        for row in range(total_row - 2) :
            for col in range(total_col - 1) :
                block_info = []
                if board[row][col] != 0 :
                    block_info.append(board[row][col])
                    block_info.append(board[row + 1][col])
                    block_info.append(board[row + 2][col])
                    block_info.append(board[row][col + 1])
                    block_info.append(board[row + 1][col + 1])
                    block_info.append(board[row + 2][col + 1])

                block_Set = set(block_info)

                if block_info.count(-1) == 2 and block_info.count(0) == 0 and len(block_Set) == 2:
                    answer += 1
                    board[row][col] = 0
                    board[row + 1][col] = 0
                    board[row + 2][col] = 0
                    board[row][col + 1] = 0
                    board[row + 1][col + 1] = 0
                    board[row + 2][col + 1] = 0

                    for idx in black_blocks :
                        x, y = idx
                        board[x][y] = 0
                    black_blocks = []
                    count = 0


    return answer
"""