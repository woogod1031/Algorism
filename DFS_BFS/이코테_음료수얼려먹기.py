n, m = list(map(int, input().split()))

field = []
visited = [[0] * m for _ in range(n)]


for _ in range(n):
  field.append(list(map(int, input())))

cnt = 0

def dfs(x,y):
  if 0 <= x < n and 0 <= y < m:
    if field[x][y] == 0 and visited[x][y] == 0:
      visited[x][y] = 1
      dfs(x+1,y)
      dfs(x-1,y)
      dfs(x,y+1)
      dfs(x,y-1)
      return True
  return False

for i in range(n):
  for j in range(m):
    if dfs(i,j) == True:
      cnt += 1

print(cnt)