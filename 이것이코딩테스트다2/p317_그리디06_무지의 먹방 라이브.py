#https://programmers.co.kr/learn/courses/30/lessons/42891

def solution(food_times, k):
    import heapq
    answer = 0
    if sum(food_times) <= k:
        return -1

    Q =[]
    for x_idx, x in enumerate(food_times):
        heapq.heappush(Q, (x, x_idx))

    sum_value = 0
    previous_step =0
    while sum_value + len(Q)*(Q[0][0] - previous_step) <= k:
        now_step, idx = heapq.heappop(Q)

        sum_value += (now_step - previous_step) * (len(Q)+1)
        previous_step = now_step

    n_Q = sorted(Q, key=lambda x: x[1])
    answer = n_Q[(k-sum_value) % len(Q)][1]

    return answer +1