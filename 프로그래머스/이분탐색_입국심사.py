#https://programmers.co.kr/learn/courses/30/lessons/43238
# 풀이 : https://lionem2018.tistory.com/entry/ProgrammersLevel-3Python-%EC%9E%85%EA%B5%AD%EC%8B%AC%EC%82%AC

def solution(n,times):
    left = 0
    answer = right = max(times) *n

    while left <= right:
        task_sum =0
        mid = (left+right) //2
        for t in times:
            task_sum += mid//t

        if task_sum < n:
            left = mid +1
        else:
            right = mid -1
            if mid <= answer:
                answer = mid
    return answer

print(solution(6, [7,10]))