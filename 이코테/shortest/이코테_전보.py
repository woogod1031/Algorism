import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, c = list(map(int, input().split()))
graph = [[] for i in range(n + 1)]

start = c

distance = [INF] * (n+1)

for _ in range(m):
  # a에서 b로가는 비용 c
  # 1 2 3
  # 1 3 2
  a,b,c = map(int, input().split())
  graph[a].append((b,c))

#------------------------setting------------------------#

queue = []

heapq.heappush(queue, (0, start))
distance[start] = 0

while queue:
  dist, now = heapq.heappop(queue)
  if distance[now] < dist:
    continue
  for i in graph[now]:
    cost = dist + i[1]
    if cost < distance[i[0]]:
      distance[i[0]] = cost
      heapq.heappush(queue, (cost, i[0]))   
      
#------------------------print------------------------#
count = 0
max_dist = 0
for d in distance:
  if d != INF:
    count += 1
    max_dist = max(max_dist, d)

print(count - 1, max_dist)