#https://programmers.co.kr/learn/courses/30/lessons/42587
#24:20~ 24:50
def solution(priorities, location):
    from collections import deque
    answer =1
    que = deque(list(zip(priorities, range(len(priorities)))))
    priorities_list = sorted(priorities)
    while que:
        p_value, p_idx = que.popleft()
        if p_idx == location and priorities_list[-1] == p_value:
            break
        elif priorities_list[-1] == p_value:
            priorities_list.pop()
            answer +=1
        else:
            que.append((p_value,p_idx))

    return answer

print(solution([1, 1, 9, 1, 1, 1], 0))