import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

q = []
start = 1

heapq.heappush(q, (0, start))
distance[start] = 0

while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for node, dt in graph[now]:
        cost = distance[now] + dt
        if cost < distance[node]:
            distance[node] = cost
            heapq.heappush(q, (cost, node))

max_node = 0
max_distance = 0
max_nodes = 0

for i in range(1, n + 1):
    if max_distance < distance[i]:
        max_distance = distance[i]
        max_node = i
        max_nodes = 1
    elif max_distance == distance[i]:
        max_nodes += 1

print(max_node, max_distance, max_nodes)
