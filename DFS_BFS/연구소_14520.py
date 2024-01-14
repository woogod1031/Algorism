n, m = map(int, input().split())
graph = []
temp = [[0] * m for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0


def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and ny >= 0 and nx < n and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)


def getSafe():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                cnt += 1
    return cnt


def solution(cnt):
    global result
    if cnt == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = graph[i][j]
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)  # 바이러스 실행 시 자동으로 다 퍼진다.
        result = max(result, getSafe())
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                cnt += 1
                solution(cnt)
                graph[i][j] = 0
                cnt -= 1


solution(0)
print(result)
