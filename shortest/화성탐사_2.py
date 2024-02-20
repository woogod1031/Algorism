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
    distance = [[INF] * n for _ in range(n)]
    for i in range(n):
        graph.append(list(map(int, input().split())))

    x, y = 0, 0
    queue = []
    heapq.heappush(queue, (graph[x][y], x, y))
    distance[x][y] = graph[x][y]

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
