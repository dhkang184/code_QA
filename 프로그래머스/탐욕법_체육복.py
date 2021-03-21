# https://programmers.co.kr/learn/courses/30/lessons/42862
# 시작시간: 00:15~

def solution(n, lost, reserve):
    answer = 0
    n_lost = list(set(lost) - set(reserve))
    n_reserve = list(set(reserve) - set(lost))
    answer = n-len(n_lost)

    for i in n_lost: #잃어버리고 여분도 없어서 빌려야 하는 학생
        if i-1 in n_reserve:
            answer += 1
            n_reserve.remove(i-1)

        elif i+1 in n_reserve:
            answer +=1
            n_reserve.remove(i+1)

    return answer