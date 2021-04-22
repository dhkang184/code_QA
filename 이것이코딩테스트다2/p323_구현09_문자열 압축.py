# https://programmers.co.kr/learn/courses/30/lessons/60057
# 12:25~ 12:45

def solution(s):
    length = len(s)
    answer = length
    for l in range(1, length//2 +1):
        now_value = s[:l]
        count =1
        new_S =""
        for x in range(l, len(s), l):
            if now_value == s[x:x+l]:
                count +=1
            else:
                if count >1:
                    new_S += str(count) + now_value
                    count =1
                else:
                    new_S += now_value
            now_value = s[x:x+l]
        if count >1:
            new_S += str(count) + now_value
        else:
            new_S += now_value
        answer = min(answer, len(new_S))

    return answer

print(solution("ababcdcdababcdcd"))