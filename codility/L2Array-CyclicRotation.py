#https://app.codility.com/c/run/trainingN97ZXS-2F9/

def solution(A, K):
    # write your code in Python 3.6

    A_len = len(A)
    #### 빈 배열 주의
    if A_len == 0:
        return A
    ## 0%0 주의!
    rotate_K = K%A_len

    if rotate_K ==0:
        return A
    else:
        return A[-rotate_K:]+ A[:rotate_K]
    pass
