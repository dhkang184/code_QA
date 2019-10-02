#https://app.codility.com/programmers/lessons/5-prefix_sums/passing_cars/

def solution(A):
    sum_A = sum(A)
    P = 0
    for idx, item in enumerate(A):
        if item ==0:
            P += sum_A
        elif item == 1:
            sum_A -=1
        if P>1000000000:
            return -1
    return P