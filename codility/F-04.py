#https://app.codility.com/programmers/lessons/99-future_training/str_symmetry_point/
# 06:25 ~

def solution(S):
    if len(S) == 1:
        return 0
    elif len(S) ==0:
        return -1
    elif len(S) %2 ==0:
        return -1

    mid_idx = len(S)//2
    for i in range(mid_idx +1):
        left_idx = i
        right_idx = -(i+1)
        if S[left_idx] != S[right_idx]:
            return -1

    return mid_idx