#https://app.codility.com/c/run/trainingQ2V8CK-QJ5/

def solution(A):
    # write your code in Python 3.6
    # min_P = 1000000000000
    # for P in range(1,len(A)):
    #     diff = sum(A[:P]) - sum(A[P:])
    #     if diff == 0:
    #         return diff
    #     if diff<0:
    #         diff = -diff
    #     if min_P >diff:
    #         min_P = diff
    #
    # return min_P

    sum_left = 0
    sum_right = sum(A)
    min_diff = None
    for P in range(1,len(A)):
        sum_left += A[P-1]
        sum_right -= A[P-1]
        diff = sum_right - sum_left
        if diff <0 :
            diff = -diff
        if min_diff == None:
            min_diff = diff
        else:
            min_diff = min(diff, min_diff)
    return min_diff