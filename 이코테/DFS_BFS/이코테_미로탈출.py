from collections import deque
n,m = list(map(int,input().split()))
field = []
visited = [ [1] * m for _ in range(n) ]

for _ in range(n):
  field.append(list(map(int, input())))

dx = [ -1, 1, 0, 0 ]
dy = [ 0, 0, -1, 1 ]

def bfs(x,y):
  que = deque()
  que.append((x,y))

  while que:
    x, y = que.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m:
        if field[nx][ny] == 1: # or visited[x][y] <= visited[nx][ny]: 지름길과 같은 특수한 경우 추가
          if visited[nx][ny] == 1:
            visited[nx][ny] = visited[x][y] + 1
            que.append((nx, ny))

  return visited[n - 1][m - 1]
            

print(bfs(0,0))


