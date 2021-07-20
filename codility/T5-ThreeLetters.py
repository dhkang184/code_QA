#https://app.codility.com/c/run/trainingPB7YRT-2NY/
"""
from itertools import permutations
def solution(A, B):
    N_list = ['a']*A + ['b']* B

    for n in list(permutations(N_list)):
        result = ''.join(n)
        if 'aaa' not in result and 'bbb' not in result:
            return result
"""

def permut(S, a, b):
    if a == 0 and b == 0:
        return S

    if a >= b:
        if a>0 and 'aaa' not in S+'a':
            ans = permut(S+'a', a-1, b)
            if ans:
                return ans
        if b>0 and 'bbb' not in S+'b':
            ans = permut(S+'b', a, b-1)
            if ans:
                return ans
    else:
        if b>0 and 'bbb' not in S+'b':
            ans = permut(S+'b', a, b-1)
            if ans:
                return ans
        if a > 0 and 'aaa' not in S + 'a':
            ans = permut(S + 'a', a - 1, b)
            if ans:
                return ans

def solution(A,B):
    return permut('', A,B)

solution(100,100)