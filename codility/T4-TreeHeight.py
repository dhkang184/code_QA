#https://app.codility.com/c/run/training9F63SU-ATF/

#from extratypes import Tree  # library with types used in the task

def solution(T):
    if T.l == None and T.r == None:
        # Has no subtree
        return 0
    elif T.l == None:
        # Only has right subtree
        return 1 + solution(T.r)
    elif T.r == None:
        # Only has left subtree
        return 1 + solution(T.l)
    else:
        # Have two subtrees
        return 1 + max(solution(T.l), solution(T.r))