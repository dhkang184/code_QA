#https://programmers.co.kr/learn/courses/30/lessons/60057
# 22:45~

def solution(s):
    answer = len(s)
    for l in range(1, int(len(s)//2)+1):
        cnt = 0
        w = s[0:l]
        l_str = ""
        for i in range(0, len(s) - l, l):
            if w == s[i:i+l]:
                cnt +=1
            else:
                if cnt ==1:
                    l_str += w
                else:
                    l_str += str(cnt) + w
                w = s[i:i+l]
                cnt = 1

        if w == s[i+l:]:
            cnt +=1
            l_str += str(cnt) + w
        else:
            if cnt == 1:
                l_str += w + s[i+l:]
            else:
                l_str += str(cnt) + w + s[i+l:]

        answer = min(answer, len(l_str))

    return answer

print(solution("xxxxxxxxxxyyy"))