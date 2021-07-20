#https://app.codility.com/programmers/trainings/5/first_unique/
from collections import defaultdict

def solution(A):

    A_dict = defaultdict(int)
    for a in A:
        A_dict[a] +=1

    for k in A_dict.keys():
        if A_dict[k] ==1:
            return k
    return -1


