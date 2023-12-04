
#   0 1 2 3 4
# 0 o o o o o
# 1 o o o o o
# 2 o o x o o
# 3 o o o o o
# 4 o o o o o

# [[o, o, o,      o, o],
#  [o, o, o,      o, o],
#  [o, o, x(2,2), o, o],
#  [o, o, o,      o, o],
#  [o, o, o,      o, o]]

dx = { 0:-1, 1:0, 2:1, 3:0,}
dy = { 0:0, 1:1, 2:0, 3:-1,}
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
n_dir = { 0:3, 3:2, 2:1, 1:0,}
# n_dir = [3,0,1,2]

n,m = list(map(int,input().split()))
a,b,d = list(map(int,input().split()))
field = []
visited = [[0 for _ in range(m)] for _ in range(n)]
# [[0] * m for _ in range(n)]

for i in range(n):  
  field.append(list(map(int,input().split())))  

visited[a][b] = 1
cnt = 1

while True:
  ps = False
  for _ in range(4):
    nx = a + dx[n_dir[d]]
    ny = b + dy[n_dir[d]]
    d = n_dir[d]
    if field[nx][ny] == 1 or visited[nx][ny] == 1:
      continue
    else:
      a, b = nx, ny
      visited[a][b] = 1      
      cnt += 1
      ps = True
      break
    
  if not ps:
    if field[a - dx[d]][b - dy[d]] == 1:
      break
    else:
      a,b = a - dx[d], b - dy[d]

print(cnt)
  


  
  


