#https://app.codility.com/programmers/lessons/4-counting_elements/max_counters/


# 정확도 : 66% , 정확도:100 , 퍼포먼스:40 빅O : O(N*M)
# def solution(N, A):
#     result = [0] * N
#     for i in A:
#         if 1 <= i <= N:
#             result[i-1] += 1
#         else:
#             result = [max(result)] * N # O(N)
#     return result


## 성공 코드 , max값을 가장 마지막에 한번만 업데이트 함
## -> max값이 나올때 마다 리스트를 새로 쓰지 않음음def solution(N, A):

    counters = N * [0]
    next_max_counter =  max_counter = 0

    for oper in A:
        if oper <= N:
            current_counter = counters[oper-1] = max(counters[oper-1] +1, max_counter+1)
            next_max_counter = max(current_counter, next_max_counter)
        else:
            max_counter = next_max_counter

    return [c if c > max_counter else max_counter for c in counters]