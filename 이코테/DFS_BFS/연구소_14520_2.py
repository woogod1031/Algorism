n, m = map(int, input().split())
graph = []
temp = [[0] * m for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, input().split())))

result = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def get_safe():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                cnt += 1
    return cnt


def spread(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        else:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                spread(nx, y)


def dfs(cnt):
    global result
    if cnt == 3:
        for i in range(n):
            for j in range(n):
                temp[i][j] = graph[i][j]
        for i in range(n):
            for j in range(n):
                if temp[i][j] == 2:
                    spread(i, j)
        safe_value = get_safe()
        result = max(result, safe_value)

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                cnt += 1
                dfs(cnt)
                cnt -= 1
                graph[i][j] = 0


dfs(0)
print(result)
