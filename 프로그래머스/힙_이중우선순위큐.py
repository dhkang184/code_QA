#https://programmers.co.kr/learn/courses/30/lessons/42628
# 24:20~ 24:35

def solution(operations):
    import heapq
    answer = []
    q =[]
    max_q =[]
    for x in operations:
        op_, value = x.split(' ')
        value = int(value)
        if op_ == "I":
            heapq.heappush(q, value)
            heapq.heappush(max_q, value*-1)
        elif value == 1 and len(q) >0:
            remove_v = heapq.heappop(max_q)
            q.remove(remove_v*-1)
        elif value ==-1 and len(q) >0:
            remove_v = heapq.heappop(q)
            max_q.remove(remove_v*-1)

    if len(q) ==0:
        return [0,0]
    else:
        return [-1*heapq.heappop(max_q), heapq.heappop(q)]
