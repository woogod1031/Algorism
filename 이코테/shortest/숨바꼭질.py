import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
INF = int(1e9)

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append((1, b))
    graph[b].append((1, a))

start = 1
q = []
heapq.heappush(q, (0, start))
distance[start] = 0

while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for dt, node in graph[now]:
        cost = dist + dt
        if distance[node] > cost:
            distance[node] = cost
            heapq.heappush(q, (cost, node))

max_node = 0
max_distance = 0
result = []

for i in range(1, n + 1):
    if max_distance < distance[i]:
        max_node = i
        max_distance = distance[i]
        result = [max_node]
    elif max_distance == distance[i]:
        result.append(i)

print(max_node, max_distance, len(result))
