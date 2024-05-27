INF = int(1e9)
n, m = map(int, input().split())

graph = [[INF]*(n + 1) for _ in range(n + 1)]

# INF INF INF INF INF INF INF
# INF 0   INF INF INF 1   INF
# INF INF 0   INF INF INF INF
# INF INF INF 0   1   INF INF
# INF INF 1   INF 0   INF 1
# INF INF 1   INF 1   0   INF
# INF INF INF INF INF INF 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1


for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


result = 0

for a in range(1, n + 1):
    cnt = 0
    for b in range(1, n + 1):
        if graph[a][b] != INF or graph[b][a] != INF:
            cnt += 1
    if cnt == n:
        result += 1

print(result)
