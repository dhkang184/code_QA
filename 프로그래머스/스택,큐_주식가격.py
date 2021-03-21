#https://programmers.co.kr/learn/courses/30/lessons/42584
# 시작 시간: 16:15 ~ 16:30

def solution(prices):
    answer = []
    for idx, p in enumerate(prices):
        ti = 0
        for n_p in prices[idx:-1]:
            if n_p < p:
                break
            else:
                ti +=1
        answer.append(ti)

    return answer

def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices) -1):
        for j in range(i+1, len(prices)):
            answer[i] +=1
            if prices[i] > prices[j] : break
    return answer



print(solution([1, 2, 3, 2, 3]))