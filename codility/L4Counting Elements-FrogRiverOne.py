#https://app.codility.com/c/run/trainingFAQF8G-6CV/

# def solution(X, A):
#     if X not in A:
#         return -1
#
#     step_A = []
#     for idx, item in enumerate(A):
#         if item not in step_A and item <= X:
#             step_A.append(item)
#         if len(step_A) == X:
#             return idx
#
#     return -1

# def solution(X, A):
#     if X not in A:
#         return -1
#
#     step_A = []
#     for idx in range(1,X+1):
#         if idx in A: #### 빅O를 크게 만듬...
#             step_A.append(A.index(idx))
#         else:
#             return -1
#     return max(step_A)

def solution(X, A):
    check = [0] * X
    check_sum = 0
    for i in range(len(A)):
        if check[A[i]-1] == 0:
            check[A[i]-1] = 1
            check_sum += 1
            if check_sum == X:
                return i
    return -1