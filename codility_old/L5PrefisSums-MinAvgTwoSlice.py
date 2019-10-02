#https://app.codility.com/programmers/lessons/5-prefix_sums/min_avg_two_slice/
def solution(A):
    if len(A) ==2:
        return 0
    for idx in range(len(A)-2):
        if idx == 0:
            min_avg = min((A[idx] +A[idx+1])/2, (A[idx] +A[idx+1]+A[idx+2])/3)
            Min_idx = idx
        else:
            if min_avg > min((A[idx] +A[idx+1])/2, (A[idx] +A[idx+1]+A[idx+2])/3):
                min_avg = min((A[idx] +A[idx+1])/2, (A[idx] +A[idx+1]+A[idx+2])/3)
                Min_idx = idx
    idx +=1
    if len(A)>2:
        if min_avg > (A[idx] + A[idx + 1]) / 2:
            Min_idx = idx
    return Min_idx