from collections import deque

n, k = map(int, input().split())
graph = [[0] * (n + 1)]
# virus = [[0] * (n + 1) for _ in range(n + 1)]
queue = []

for i in range(1, n + 1):
    li = list(map(int, input().split()))
    for j in range(1, len(li) + 1):
        if li[j - 1] >= 1:
            queue.append((li[j - 1], i, j))
    graph.append([0, *li])

queue.sort(key=lambda x: x[0])
queue = deque(queue)

s, x, y = map(int, input().split())
# 바이러스는 1초마다 상, 하, 좌, 우의 방향으로 증식
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

# 낮은 종류의 바이러스부터 먼저 증식
# 어떠한 바이러스가 존재한다면, 그 곳에는 다른 바이러스가 들어갈 수 없다.

# S초가 지난 후에 (X,Y)에 존재하는 바이러스의 종류를 출력


def virus(num, x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 1 and ny >= 1 and nx <= n and ny <= n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = num
                queue.append((num, nx, ny))


for k in range(1, s+1):
    for i in range(len(queue)):
        num, nx, ny = queue.popleft()
        virus(num, nx, ny)

print(graph[x][y])
