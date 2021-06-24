#https://programmers.co.kr/learn/courses/30/lessons/42626
# 22:20~ 22:40
"""
heapq 사용시 초기 리스트 그대로 쓰지 말고 함수 1회 정렬 하기
"""

def solution(scoville, K):
    answer = 0
    import heapq
    q = []### 정렬 리스트 생성
    for x in scoville:
        heapq.heappush(q, x)

    while True:
        if len(q) == 1 and q[0] < K:
            return -1
        v1 = heapq.heappop(q)
        if v1 >= K:
            break
        else:
            answer +=1
            v2 = heapq.heappop(q)
            new_v = v1+(v2*2)
            heapq.heappush(q, new_v)

    return answer

print(solution([1,1,1,2,3,45], 3))