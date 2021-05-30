#20:50 ~ 23:10
# https://app.codility.com/programmers/lessons/8-leader/dominator/

def solution(A):
    dict_A = {}
    dict_idx = {}
    max_num = 0
    max_idx = 0
    for x_idx, x in enumerate(A):
        if x not in dict_A:
            dict_A[x] =1
            dict_idx[x] = [x_idx]
        else:
            dict_A[x] = dict_A[x] +1
            idx_list = dict_idx[x]
            idx_list.append(x_idx)
            dict_idx[x] = idx_list
        if max_num < dict_A[x]:
            max_num = dict_A[x]
            max_idx = x_idx
    if max_num > len(A)//2:
        return max_idx
    else:
        return -1

solution([0,0,1,1,1])