#https://app.codility.com/programmers/trainings/5/disappearing_pairs/

def solution(S):
    # write your code in Python 3.6
    stack = []
    for s in S:
        if len(stack) == 0:
            stack.append(s)
        else:
            if s == stack[-1]:
                stack.pop()
            else:
                stack.append(s)
    return ''.join(stack)
