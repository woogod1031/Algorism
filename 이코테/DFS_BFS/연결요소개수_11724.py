n, m =  list(map(int, input().split()))
graph = [[] for  _ in range(n+1)]

cnt = 0

visited = [False for _ in range(n+1)]

for _ in range(m):
  a,b = list(map(int, input().split()))
  graph[a].append(b)
  graph[b].append(a)

def dfs(graph, v, visited):            
  if visited[v] == True:
    return
  visited[v] = True
  for i in graph[v]:
    dfs(graph, i, visited)  

for j in range(1, n+ 1):
  if not visited[j]:
    cnt += 1
    dfs(graph, j, visited)

print(cnt)      