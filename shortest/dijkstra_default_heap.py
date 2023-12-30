import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드 수(6), 간선 수(11)
n, m = map(int, input().split())
# 시작 노드(1)
start = int(input())
graph = [[] for i in range(n + 1)]
# 최단 거리 초기화
distance = [INF] * (n+1)

# 간선 입력
# 1 2 2
# 1 3 5
# 1 4 1

# 2 3 3
# 2 4 2

# 3 2 3
# 3 6 5

# 4 3 3
# 4 5 1

# 5 3 1
# 5 6 2
for _ in range(m):
  # a에서 b로가는 비용 c
  a,b,c = map(int, input().split())
  graph[a].append((b,c))

#------------------------setting------------------------#
def dijkstra(start):
  queue = []
  # heapq에서 튜플의 첫번째 원소를 기준으로 우선순위를 정한다.
  # 따라서 최단거리를 추출하기 위해 튜플은 (거리(0), 노드(1))로 구성된다.
  heapq.heappush(queue, (0, start))
  distance[start] = 0 

  while queue:
    dist, cur_node = heapq.heappop(queue)
    if distance[cur_node] < dist:
      continue
    for nd, di in graph[cur_node]:
      cost = dist + di
      if cost < distance[nd]:
        distance[nd] = cost
        heapq.heappush(queue, (cost, nd)) 
      
dijkstra(start)

#------------------------print------------------------#
for i in range(1, n + 1):
  if distance[i] == INF:
    print("INFINITY")
  else:
    print(distance[i])
