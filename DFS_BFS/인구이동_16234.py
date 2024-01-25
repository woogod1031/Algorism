from collections import deque
import sys
input = sys.stdin.readline

n, l, r = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

days = 0
q = deque()


def bfs(start_x, start_y, visited):
    global graph

    q.append((start_x, start_y))
    union = []
    union.append((start_x, start_y))
    while q:
        qx, qy = q.popleft()
        for i in range(4):
            nx = qx+dx[i]
            ny = qy+dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n and visited[nx][ny] == 0:
                if l <= abs(graph[qx][qy] - graph[nx][ny]) <= r:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    union.append((nx, ny))
    if len(union) <= 1:
        return 0
    result = sum(graph[x][y] for x, y in union)//len(union)  # 연합 인구 수 계산
    for x, y in union:
        graph[x][y] = result
    return 1


while True:
    stop = 0
    visited = [[0]*n for _ in range(n)]
    q = deque()
    opened_nations = []
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                stop += bfs(i, j, visited)
    if stop == 0:
        break
    days += 1

print(days)
