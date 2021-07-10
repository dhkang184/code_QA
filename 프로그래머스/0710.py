from collections import deque
import heapq


def solution(priorities, location):
    answer = 0

    q = deque()
    heap_q = []
    for p_idx, p in enumerate(priorities):
        q.append((p, p_idx))
        heapq.heappush(heap_q,(-p, p_idx))
    while True:
        c_q, c_idx = q.popleft()
        h_q, h_idx = heapq.heappop(heap_q)
        h_q = -h_q
        if c_q != h_q:
            q.append((c_q, c_idx))
            heapq.heappush(heap_q, (-h_q, h_idx))
        else:
            answer +=1
            if c_idx == location:
                break

    return answer

print(solution([2,1,3,2], 2))