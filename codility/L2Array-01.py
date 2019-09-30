#https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/

def solution(A):
    # write your code in Python 3.6
    while True:
        item = A.pop(0)
        if item in A:
            A.pop(A.index(item))
        else:
            return item
    pass

def test3(A):
    if len(A) == 1:
        return A[0]

    A = sorted(A)
    for i in range(0, len(A), 2):
        if i+1 == len(A):
            return A[i]
        if A[i] != A[i+1]:
            return A[i]
