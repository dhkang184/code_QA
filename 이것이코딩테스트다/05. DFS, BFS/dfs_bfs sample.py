#DFS 방법 정의 (재귀함수)
def dfs(graph, v, visited):
    visited[v] = True  # 현재 노드를 방문 처리
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

from collections import deque
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

    graph = [
        [],
        [2,3,8],
        [1,7],
        [1,4,5],
        [3,5],
        [3,4],
        [7],
        [2,6,8],
        [1,7]]
    visited = [False]*9 #각 노드가 방문된 정보 리스트 생성
    bfs(graph, 1, visited)
    dfs(graph, 1, visited)
