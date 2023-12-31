from collections import deque

# 노드 개수, 간선 개수
v, e = map(int, input().split())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    # a to b로 연결된 간선이므로 b의 진입차수를 1 증가시킨다.
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

# ------------------------setting------------------------#


def topology_sort():
    result = []
    q = deque()

    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    # 진입차수가 0인 노드부터 시작해서 q가 빌 떄 까지 진행
    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    # 알고리즘 수행 결과 출력
    for i in result:
        print(i, end=' ')

# ------------------------define------------------------#


topology_sort()

# ------------------------excute------------------------#
