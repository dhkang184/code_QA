#01:35~
#

def solution(A):
    L = len(A)

    A = list(set(sorted(A)))
    if A[-1] == A[0] + L-1 and L == len(A) and A[0] ==1:
        return 1
    else:
        return 0