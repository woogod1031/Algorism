from sys import stdin

n, m = list(map(int, stdin.readline().split()))
graph = []
visited = [[0] * m for _ in range(n)]
r, c, d = list(map(int, stdin.readline().split()))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(n):
    graph.append(list(map(int, stdin.readline().split())))

visited[r][c] = 1
cnt = 1


def check(x, y):
    global n, m,graph,visited
    if 0 <= x < n and 0 <= y < m and graph[x][y] == 0 and visited[x][y] == 0:
        return True
    else:
        return False


def operating():
    global r,c,d,cnt
    while True:
        isClean = False
        for _ in range(4):
            nx = r + dx[(d + 3) % 4]
            ny = c + dy[(d + 3) % 4]
            d = (d + 3) % 4
            if check(nx, ny):
                visited[nx][ny] = 1
                cnt += 1
                r = nx
                c = ny
                isClean = True
                break

        if not isClean:
            if graph[r - dx[d]][c - dy[d]] == 1:
                print(cnt)
                break
            else:
                r, c = r - dx[d], c - dy[d]

operating()
