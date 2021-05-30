#20:50~
#https://app.codility.com/c/run/trainingQ588XD-AKA/
def solution(A):
    import itertools
    A = sorted(A)
    if len(A) >=6:
        n_list = list(itertools.combinations([A[0], A[1], A[2], A[-1], A[-2], A[-3]], 3))
    else:
        n_list = list(itertools.combinations(A, 3))
    answer = A[0] * A[1] * A[2]
    for x in n_list:
        answer = max((x[0] * x[1] * x[2]), answer )

    if answer <0 and 0 in A:
        answer =0
    return answer





