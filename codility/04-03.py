#01:30~ 1:35
#https://app.codility.com/c/run/training9PDYVD-CQ7/

def solution(A):
    A = sorted(A)
    answer =1
    for x in A:
        if x == answer:
            answer +=1
        elif x> answer:
            return answer
    return answer