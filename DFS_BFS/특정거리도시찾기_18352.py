n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)


def search(graph, visited, node):
    for i in graph[node]:  # 2, 3
        if visited[i] == 0:
            visited[i] = visited[node] + 1
            search(graph, visited, i)
        else:
            visited[i] = min(visited[node] + 1, visited[i])
            search(graph, visited, i)


search(graph, visited, x)
answer = []
for i in range(1, n + 1):
    if visited[i] == k:
        answer.append(i)

if len(answer) == 0:
    print(-1)
else:
    for i in answer:
        print(i, end='\n')
