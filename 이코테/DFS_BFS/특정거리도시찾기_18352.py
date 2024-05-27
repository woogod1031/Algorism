import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n+1)
start = x

# 모든 비용은 1로 다 같다.
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))


def dijkstra(start_node):
    queue = []
    heapq.heappush(queue, (0, start_node))
    distance[start_node] = 0

    while queue:
        cur_distance, cur_node = heapq.heappop(queue)
        if distance[cur_node] < cur_distance:
            continue
        for child_node, child_distance in graph[cur_node]:
            new_distance = cur_distance + child_distance
            if new_distance < distance[child_node]:
                distance[child_node] = new_distance
                heapq.heappush(queue, (new_distance, child_node))


dijkstra(start)

answer = []
for i in range(1, n + 1):
    if distance[i] == k:
        answer.append(i)

if len(answer) == 0:
    print(-1)
else:
    for i in answer:
        print(i, end='\n')
