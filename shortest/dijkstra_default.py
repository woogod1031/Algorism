import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드 수(6), 간선 수(11)
n, m = map(int, input().split())
# 시작 노드(1)
start = int(input())
graph = [[] for i in range(n + 1)]

# 방문 여부
visited = [False] * (n+1)
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
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# ------------------------setting------------------------#


def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i

    return index


def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    for _ in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            # 만약 graph[4]일 떄: graph[4] = [(3, 3), (5, 1)]
            # 1 => 4 => 3 값이: cost = distance[now] + j[1]
            # 1 => 3 값보다 작으면: cost < distance[j[0]]:
            # 3까지 가는 최단경로를 변경해준다: distance[j[0]] = cost
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost


dijkstra(start)
# ------------------------print------------------------#
for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
