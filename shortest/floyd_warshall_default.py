INF = int(1e9)
# 노드 수, 간선 수
n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n+1)]

for k in range(1, n + 1):
  for a in range(1, n + 1):
    if k == a:
      graph[k][a] = 0

for _ in range(m):
  # a에서 b로가는 비용 c
  a,b,c = map(int, input().split())
  graph[a][b] = c

#------------------------setting------------------------#

for k in range(1, n + 1):
  for a in range(1, n + 1):
    for b in range(1, n + 1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b]) 

# a에서 b까지 가는 비용과 k를 거치고 가는 비용을 비교한다.

#------------------------print------------------------#

for a in range(1, n + 1):
  for b in range(1, n + 1):
    if graph[a][b] == INF:
      print("INFINITY", end=' ')
    else:
      print(graph[a][b], end=' ')
  print()