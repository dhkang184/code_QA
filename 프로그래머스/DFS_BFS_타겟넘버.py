#https://programmers.co.kr/learn/courses/30/lessons/43165
# 시작시간: 00:15~ 00:30

def solution(numbers, target):
    global answer
    answer = 0

    def dfs(numbers, num,i):
        global answer
        if i == len(numbers):
            if num == target:
                answer +=1
            return
        dfs(numbers, num+numbers[i], i+1)
        dfs(numbers, num-numbers[i], i+1)

    dfs(numbers,0,0)

    return answer

print(solution([1,1,1,1,1],3))