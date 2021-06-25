#https://programmers.co.kr/learn/courses/30/lessons/43162
#22:10~ 22:20
"""
def solution(n, computers):
    from collections import deque
    answer = 0

    visited = [False] * n
    q = deque()
    for x in range(n):
        if visited[x] == False:
            visited[x] = True
            answer +=1
            q.append(x)
            while q:
                val = q.popleft()
                for y_idx, y in enumerate(computers[val]):
                        if y == 1 and visited[y_idx] == False:
                            visited[y_idx] =True
                            q.append(y_idx)

    return answer
"""


def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]
    def dfs(computers, visited, start):
        stack = [start]
        while stack:
            j = stack.pop()
            if visited[j] == 0:
                visited[j] = 1
            # for i in range(len(computers)-1, -1, -1):
            for i in range(0, len(computers)):
                if computers[j][i] ==1 and visited[i] == 0:
                    stack.append(i)
    i=0
    while 0 in visited:
        if visited[i] ==0:
            dfs(computers, visited, i)
            answer +=1
        i+=1
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))