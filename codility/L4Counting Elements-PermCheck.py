#https://app.codility.com/programmers/lessons/4-counting_elements/perm_check/

def solution(A):
    # write your code in Python 3.6
    len_A = len(A)
    set_A = sorted(list(set(A)))
    if set_A[0] == 1 and set_A[-1] == len_A and len_A == len(set_A):
        return 1
    else:
        return 0
