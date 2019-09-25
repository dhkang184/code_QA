#https://app.codility.com/programmers/lessons/4-counting_elements/missing_integer/
def solution(A):
    check_A = [0] * (len(A)+1)
    for item in A:
        if 0< item <= len(A):
            check_A[item -1] =1
    return check_A.index(0)+1