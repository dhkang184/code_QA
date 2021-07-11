#https://programmers.co.kr/learn/courses/30/lessons/49189
"""
from collections import deque

def bfs(v, visited, adj):
    count = 0
    q = deque([[v, count]])
    while q:
        value = q.popleft()
        v = value[0]
        count = value[1]
        if visited[v] == -1:
            visited[v] = count
            count += 1
            for e in adj[v]:
                q.append([e, count])

def solution(n, edge):
    answer = 0
    visited = [-1] * (n + 1)
    adj = [[] for _ in range(n + 1)]
    for e in edge:
        x = e[0]
        y = e[1]
        adj[x].append(y)
        adj[y].append(x)
    bfs(1, visited, adj)
    for value in visited:
        if value == max(visited):
            answer += 1
    return answer
"""

def solution(n, edge):
    from collections import deque
    answer = 0
    adj = [[] for x in range(n + 1)]
    for e in edge:
        adj[e[0]].append(e[1])
        adj[e[1]].append(e[0])

    step_list = [-1] * (n + 1)
    step_list[1] = 0
    q = deque([1])

    while q:
        c_v = q.popleft()
        c_count = step_list[c_v]
        for next_v in adj[c_v]:
            if step_list[next_v] == -1:
                step_list[next_v] = c_count + 1
                q.append(next_v)
    answer = step_list.count(max(step_list))

    return answer