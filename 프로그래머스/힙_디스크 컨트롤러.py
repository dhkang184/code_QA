#https://programmers.co.kr/learn/courses/30/lessons/42627

#시작 시간: 18:15 ~ 18:55

def solution(jobs):
    import heapq
    answer = 0
    c_t = 0
    total_t = 0

    heap_list = []
    for x in jobs:
        heapq.heappush(heap_list, x)

    while heap_list:
        c_data = heapq.heappop(heap_list)
        sub_heap =[]
        if c_data[0] >= c_t:
            c_t = c_data[0] + c_data[1]
            total_t += c_data[1]
        else:
            heapq.heappush(sub_heap, [c_data[1],c_data[0]])
            while heap_list:
                if heap_list[0][0] >= c_t:
                    break
                sub_data = heapq.heappop(heap_list)
                heapq.heappush(sub_heap, [sub_data[1], sub_data[0]])
            n_data = heapq.heappop(sub_heap)
            total_t += c_t + n_data[0] - n_data[1]
            c_t += n_data[0]

            while sub_heap:
                r_data = heapq.heappop(sub_heap)
                heapq.heappush(heap_list, [r_data[1],r_data[0]])

    answer = total_t//len(jobs)

    return answer

print(solution([[0, 3], [1, 9], [2, 6]]))