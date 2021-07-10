#https://app.codility.com/c/run/trainingSJCWPW-5V4/
#24:10~ 24:15

def solution(A):
    sum_a = sum(A)
    n = len(A) +1
    ans = (n*(n+1))//2
    return ans - sum_a
