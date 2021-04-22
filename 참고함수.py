#순열 조합 , :https://shoark7.github.io/programming/algorithm/Permutations-and-Combinations

import itertools
mylist = [1,2,3]
result = itertools.combinations(mylist, r=2)
result = itertools.combinations_with_replacement(mylist, r=2)



from collections import deque
que = deque(['bb','cc'])
que.append('aaa')
que.popleft()

#회전
def rotate_90(map):
    N = len(map)
    rot = [[0] *N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            rot[c][N-1-r] = map[r][c]

    return rot

def rotate_180(map):
    N = len(map)
    rot = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            rot[N-1-r][N - 1 - c] = map[r][c]

    return rot

def rotate_270(map):
    N = len(map)
    rot = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            rot[N-1-c][r] = map[r][c]

    return rot


# DFS
def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# BFS
def bfs(graph, start, visited):
    from collections import deque
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 정렬 quick sort
def quick_sort(array, start, end):
    if start>= end:
        return
    pivot = start
    left = start +1
    right = end

    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left +=1

        while right > start and array[right] >= array[pivot]:
            right -=1

        if left >right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

        quick_sort(array, start, right-1)
        quick_sort(array, right+1, end)

# 최단거리 _ 다익스트라 알고리즘
n =10
distance = [1e9] * n # 10: 노드 개수
graph = [[] for i in range(n+1)]
def dijksta(start):
    import heapq
    q = []
    heapq.heappush(q, (0,start))
    while q:
        now, dist = heapq.heappop()
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))

#최소 신장 트리
"""
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화하기

# 모든 간선을 담을 리스트와, 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# 모든 간선에 대한 정보를 입력 받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
"""

