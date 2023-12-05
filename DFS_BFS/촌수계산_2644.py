from collections import deque

n = int(input())

people = [[] for _ in range(n + 1)]
checked = [[False] for _ in range(n + 1)]

a, b = list(map(int, input().split()))

m = int(input())
for i in range(m):
  x, y = list(map(int, input().split()))  
  people[x].append(y)
  people[y].append(x)

def bfs():    
  que = deque()
  que.append(([a], 0))
  while que:
    node, cnt = que.popleft()  
    for i in node:
      if checked[i] == True:
        continue
      else:
        if i == b:               
          return cnt  
        checked[i] = True
        que.append((people[i], cnt + 1))        
  return -1

print(bfs())