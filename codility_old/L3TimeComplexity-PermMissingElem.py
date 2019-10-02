#https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/
# def solution(A):
#     # write your code in Python 3.6
#     A = sorted(A)
#     for idx in range(len(A)):
#         if idx+1 != A[idx]:
#             return idx +1
#     pass

def solution(A):
    return sum (range(len(A)+2)) - sum(A)