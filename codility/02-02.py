#https://app.codility.com/c/run/trainingRYFRQ7-RFZ/
# 22:55~ 23:05

def solution(A):
    # write your code in Python 3.6
    A = sorted(A)
    for x in range(0, len(A), 2):
        if x+1 >= len(A):
            return A[x]

        if A[x] != A[x+1]:
            return A[x]
    return A[-1]