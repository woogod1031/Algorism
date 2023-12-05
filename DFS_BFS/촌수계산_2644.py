from collections import deque

n = int(input())
people = [[] for _ in range(n + 1)]
visited = [[False] for _ in range(n + 1)]
a, b = list(map(int, input().split()))
m = int(input())

for i in range(m):
  x, y = list(map(int, input().split()))  
  people[x].append(y)
  people[y].append(x)

connenct = False
cnt = 0

que = deque()
que.append(([a], cnt))

while que:
  v, c = que.popleft()  
  for i in v:
    if visited[i] == True:
      continue
    else:
      visited[i] = True
      que.append((people[i], c + 1))
      if i == b:
        connenct = True   
        cnt = c
        break
  if connenct == True:
    break

if connenct == True:
  print(cnt)
else:
  print(-1)