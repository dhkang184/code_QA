#https://app.codility.com/c/run/trainingQXRMU7-8SG/
#22:35~ 22:43

def solution(S):
    # write your code in Python 3.6
    stack = []
    for x in S:
        if len(stack) ==0:
            stack.append(x)
        elif x ==")" and stack[-1] == "(":
            stack.pop()
        elif x =="]" and stack[-1] == "[":
            stack.pop()
        elif x == "}" and stack[-1] == "{":
            stack.pop()
        else:
            stack.append(x)

    if len(stack) ==0:
        return 1
    else:
        return 0
    pass

print(solution("))))"))