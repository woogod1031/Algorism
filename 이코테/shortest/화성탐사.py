import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

t = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(t):
    n = int(input())
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))
    distance = [[INF] * (n) for _ in range(n)]

    x, y = 0, 0
    queue = []
    heapq.heappush(queue, (graph[x][y], x, y))
    distance[x][y] = graph[x][y]

    # queue에는 노드의 값, 해당 노드의 좌표로 이루어져 있다.
    # 노드의 값이 현재 등록되어있는 최단거리보다 큰 경우는, 즉 한 번 들렸던 경우는 패스,
    # 아니면 노드의 4방위에 해당하는 위치의 최단거리를 구해준다.
    # 현재 등록되어이있는 최단거리보다 새로 구한 거리가 더 짧으면 갱신해주고
    # queue에 넣어서 다음
    while queue:
        dist, x, y = heapq.heappop(queue)
        if distance[x][y] < dist:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            cost = dist + graph[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(queue, (cost, nx, ny))

    print(distance[n-1][n-1])
