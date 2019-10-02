#https://app.codility.com/programmers/lessons/5-prefix_sums/count_div/
def solution(A,B,K):
    if A%K == 0:
        start_K = A
    else:
        start_K = A + (K - A%K)

    if B<start_K:
        return 0

    if B%K == 0:
        END_N = B
    else:
        END_N = B - B%K

    return int(END_N/K - start_K/K +1)