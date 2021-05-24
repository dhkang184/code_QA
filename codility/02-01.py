#https://app.codility.com/c/run/trainingUY4RF8-JA5/
#22:35~ 22:45

def solution(A, K):
    # write your code in Python 3.6
    if len(A) ==0:
        return A
    K = K%len(A)
    A = A[len(A)-K:] + A[:len(A)-K]

    return A