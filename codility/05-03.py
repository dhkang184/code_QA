# 10:45~

def solution(A):
    slice_size = 2
    if len(A) == 2:
        return 0

    min_value = 1e9
    min_idx = 0

    for x in range(slice_size, len(A) +1):
        for y in range(len(A) -x):
            if min_value > sum(A[y:y+x])/x:
                min_value = sum(A[y:y+x])/x
                min_idx = y
            if min_value == sum(A[y:y+x])/x:
                min_idx = min(min_idx,y)
    return min_idx

A = [4,2,2,5,1,5,8]

solution(A)