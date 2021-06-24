#https://programmers.co.kr/learn/courses/30/lessons/43165
# 24:40~ 01:00

def solution(numbers, target):
    from collections import deque
    q = deque([0])
    for x in numbers:
        q_len = len(q)
        for i in range(q_len):
            val = q.popleft()
            q.append(val + x)
            q.append(val - x)
    answer =0
    # for y in q:
    #     if y == target:
    #         answer +=1
    q.count(target)
##
    return answer

print(solution([1,1,1,1,1],3))