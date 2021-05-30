#12:05 ~12:20
#

def solution(S):
    end_dict = {")":"(",
              "]":"[",
              "}":"{",
              }
    stack_list = []
    for x in S:
        if x in end_dict:
            if len(stack_list) ==0:
                return 0
            if end_dict[x] == stack_list[-1]:
                stack_list.pop()
            else:
                return 0
        else:
            stack_list.append(x)
    if len(stack_list) ==0:
        return 1
    else:
        return 0