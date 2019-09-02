# https://www.welcomekakao.com/learn/courses/30/lessons/42894

"""
파이썬 2차원 배열 만들기
w, h = 8, 5.
Matrix = [[0 for x in range(w)] for y in range(h)]

"""

def check_shape(cur_w, cur_h,max_w, max_h, num, matrix):
    dw = [[1,2,2], [1,0,0], [0,1,2], [0,0,-1],
          [1,2,0], [0,0,1], [0,-1,-2],[1,1,1],
          [-1,0,1], [0,0,1], [1,2,1],[0,0,-1]
          ]
    dh = [[0,0,1], [0,1,2], [1,1,1], [1,2,2],
          [0,0,1], [1,2,2], [1,1,1], [0,1,2],
          [1,1,1], [1,2,1], [0,0,1], [1,2,1]
          ]
    for idx in range(len(dw)):
        check_count =0
        for s_idx in range(3):
            check_w = cur_w + dw[idx][s_idx]
            check_h = cur_h + dh[idx][s_idx]
            if check_h >-1 and check_w> -1 and check_h <= max_h and check_w <=max_w:
                if matrix[check_w][check_h] == num:
                    check_count += 1
                    if check_count == 3:
                        return idx
                else:
                    check_count = 0
                    break
            else:
                check_count = 0
                break

def masking(mask_matrix, num, cur_w, cur_h):
    max_h = len(mask_matrix) -1
    if num in [0,4,10] :
        for idx in range(max_h - cur_h):
            mask_matrix[cur_w][cur_h+idx] = -1
            mask_matrix[cur_w+1][cur_h+idx] = -1
            mask_matrix[cur_w+2][cur_h+idx] = -1
    if num in [1,7] :
        for idx in range(max_h - cur_h):
            mask_matrix[cur_w][cur_h+idx] = -1
            mask_matrix[cur_w+1][cur_h+idx] = -1

def solution(board):
    answer = 0
    h = len(board)
    w = len(board[0])
    mask_matrix = [[0 for x in range(w)] for y in range(h)]
    check_dict = {}
    for cur_h in range(h):
        for cur_w in range(w):
            if board[cur_w][cur_h] >0 and board[cur_w][cur_h] not in check_dict:
                num = check_shape(cur_w,cur_h,w,h,board[cur_w][cur_h], board)
                check_dict[num] = [cur_w, cur_h]


    return answer