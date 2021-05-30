#20:30~20:45
#https://app.codility.com/c/run/trainingAC8VJM-RCG/
def solution(A):
    answer = 0
    sum_A = sum(A)

    for x in A:
        if x == 0:
            answer += sum_A
        else:
            sum_A -=1
        if answer > 1000000000:
            return -1

    return answer


