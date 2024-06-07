import sys

computer_num = int(sys.stdin.readline()) #7
edge_num = int(sys.stdin.readline()) #6

graph = [[] for _ in range(computer_num + 1)] # 0 ~ 7 => 8개
#graph = [ [],[],[],[],[],[],[],[] ]
for _ in range(edge_num): # 0 ~ 5

    a, b = map(int,sys.stdin.readline().split())
    #[1 2],[2,3],[1,5],[5,2],[5,6],[4,7],
    
    graph[a].append(b) #a위치에 a랑 연결된 걸 집어넣는다
    graph[b].append(a) #b위치에 a랑 연결된 걸 집어넣는다
#graph = [ [],[2,5],[1,3,5],[2],[7],[1,2,6],[5],[4] ]
visited = []
# visited =
# [False],[False],[False],[False],[False],[False],[False],[False]

def dfs(graph, cur_node, visited): #시작 cur은 1
    # 현재 노드를 방문처리
    visited.append(cur_node)
    graph[cur_node].sort()
    # 현재 노드와 인접한 노드를 확인
    for link_node in graph[cur_node]: #2,5
        # 방문하지 않은 노드라면 재귀호출
        if link_node not in visited:
            dfs(graph, link_node, visited)
 
dfs(graph, 1, visited)
print(len(visited)-1) #1 컴퓨터 제외







