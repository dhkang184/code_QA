#09:50~ 10:15
#

def solution(A,B,K):
    if A%K == 0:
        start_K = A
    else:
        start_K = A + (K - A%K)

    if B%K == 0:
        END_N = B
    else:
        END_N = B - B%K

    if END_N < start_K:
        return 0

    return int(END_N/K - start_K/K +1)
"""
def solution(A, B, K):
    start_num = A
    end_num = B
    if A%K ==0:
        start_num = A
    else:
        start_num = A + (A%K)

    if start_num >B:
        return 0
    elif B%K ==0:
        end_num = B

    return(end_num//K - start_num//K +1)
"""