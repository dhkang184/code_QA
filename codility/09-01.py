# 12:05 ~
from collections import deque
def solution(A):
    answer = 0
    front_sum = [0] * len(A)
    back_sum = [0] * len(A)
    for x in range(1,len(A)-2):
        if front_sum[x-1] + A[x] >0:
            front_sum[x] = front_sum[x-1] + A[x]

    for x in range(len(A)-2, 1, -1):
        if back_sum[x+1] + A[x] >0:
            back_sum[x] = back_sum[x+1] + A[x]

    for x in range(1, len(A) -1):
        answer = max(answer, front_sum[x]+back_sum[x])
    return answer

solution([0,10,-5,-2,0])