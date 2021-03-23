# https://programmers.co.kr/learn/courses/30/lessons/42747
# 24:50~ 24:55

def solution(citations):
    answer = len(citations)
    citations.sort()
    for x in range(len(citations)):
        if citations[x] >= answer:
            return answer
        else:
            answer -=1
    return answer

print(solution([3,0,6,1,5]))