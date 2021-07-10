#24:15~ 24:50
#https://app.codility.com/c/run/trainingXQZBBU-6W2/

def solution(A):

    if len(A) == 2:
        return(abs(A[0]-A[1]))
    R_A = sum(A[1:])
    L_A = A[0]
    answer = abs(R_A - L_A)
    for x in range(1, len(A)-1):
        R_A -= A[x]
        L_A += A[x]
        answer = min(answer, abs(R_A - L_A))

    return answer