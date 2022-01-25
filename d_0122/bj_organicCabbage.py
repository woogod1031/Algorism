import sys
sys.setrecursionlimit(10**9)

test = int(sys.stdin.readline()) # 테스트케이스 2개

result_list = []

def make_graph(m, n, k):
    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        graph[y][x] = '1'
    return graph

def dfs(i,j):
        if( i < 0 or i >= len(graph) or \
            j < 0 or j >= len(graph[0]) or \
            graph[i][j] != '1'): #0이면 return
            return
        
        graph[i][j] = 0 #0만들어주고

        dfs(i,j+1) #상하좌우 검사
        dfs(i,j-1)
        dfs(i-1,j)
        dfs(i+1,j)
        
for _ in range(test):
    result = 0
    m, n, k = map(int, sys.stdin.readline().split())
    graph = make_graph(m, n, k)

    for i in range(len(graph)): # 8
        for j in range(len(graph[0])): #10
            if graph[i][j] == '1':
                dfs(i,j)
                result += 1

    result_list.append(result)

print(*result_list, sep='\n')

#for i,j in row[1]
#    if i,j 이 1이면:
#        1,1 값을 0으로 바꾸고
#
#        dfs(i,j+1) #주변값중에 1이 있으면 0으로
#        dfs(i,j-1)
#        dfs(i+1,j)
#        dfs(i-1,j)