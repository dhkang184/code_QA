# page 251
"""
다익스트라 알고리즘: 한 지점에서 다른 특정 지점까지의 최단 경로를 구할 때 사용
플로이드 워셜 알고리즘: 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우
"""

#소스 코드: page.257

def floyd():
    INF = int(1e9)

    n = int(input()) #n: 노드의 개수
    m = int(input()) #m: 간선의 개수

    graph = [[INF]*(n+1) for _ in range(n+1)]

    # 자기 자신은 0으로
    for a in range(1,n+1):
        for b in range(1, n+1):
            if a==b:
                graph[a][b] = 0

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a][b] =c

    for k in range(1, n+1):
        for a in range(1,n+1):
            for b in range(1, n+1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    # 수행 결과
    for a in range(1, n+1):
        for b in range(1, n+1):
            if graph[a][b] == INF:
                print("INF", end = " ")
            else:
                print(graph[a][b], end=" ")
    print()

