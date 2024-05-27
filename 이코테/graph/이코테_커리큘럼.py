from collections import deque
import copy

# 노드 개수, 간선 개수
v = int(input())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for _ in range(v + 1)]
# 강의 시간 초기화
time = [0] * (v + 1)

for i in range(1, v + 1):
    data = list(map(int, input().split()))
    # 강의 시간
    time[i] = data[0]
    for x in data[1:-1]:
        # 선수 과제 번호 추가
        indegree[i] += 1
        graph[x].append(i)


def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    # 진입차수가 0인 노드부터 시작해서 q가 빌 떄 까지 진행
    while q:
        cur_node = q.popleft()
        # cur_node를 진입 차수로 갖고 있는 것들, 즉 cur_node 와 엮여있는것들 호출
        for i in graph[cur_node]:
            result[i] = max(result[i], result[cur_node] + time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    # 알고리즘 수행 결과 출력
    for i in range(1, v + 1):
        print(result[i])


topology_sort()
