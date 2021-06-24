#https://programmers.co.kr/learn/courses/30/lessons/42627
# 22:45~ 23:45

def solution(jobs):
    import heapq
    answer = 0

    q = []
    for x in jobs:
        heapq.heappush(q, x)

    jobs_num = len(jobs)
    end_time = 0
    req_time = 0
    working_time =0

    temp_list = []
    while q:
        # q의 값 중 첫번째 값 앞에 진행되고 있는것이 없을경우
        c_value = heapq.heappop(q)
        if c_value[0] >= end_time:
            req_time = c_value[0]
            end_time = req_time + c_value[1]
            working_time += (end_time-req_time)

        # q 값 중 첫번째 값을 처리 하기 전 프로세스가 진행 중일 경우
        else:
            # sub list 생성
            temp_list.append(c_value)
            while q:
                temp_value = heapq.heappop(q)
                if temp_value[0] < end_time:
                    temp_list.append(temp_value)
                else:
                    heapq.heappush(q,temp_value)
                    break
            temp_list = sorted(temp_list, key= lambda x:(-x[1],-x[0]))
            c_value = temp_list.pop()
            req_time = c_value[0]
            end_time = end_time + c_value[1]
            working_time += (end_time - req_time)
            for y in temp_list:
                heapq.heappush(q, y)
            temp_list = []

    return working_time//jobs_num

print(solution([[0, 3], [1, 9], [2, 6]]	))