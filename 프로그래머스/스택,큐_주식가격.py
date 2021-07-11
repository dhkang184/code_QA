from collections import deque


def solution(prices):
    answer = [0] * len(prices)

    for x_idx, x in enumerate(prices):
        for j_idx in range(x_idx, len(prices)):
            if x > prices[j_idx] or j_idx == len(prices) -1:
                answer[x_idx] = j_idx - x_idx
                break

    return answer

print(solution([1,2,3,2,3]))