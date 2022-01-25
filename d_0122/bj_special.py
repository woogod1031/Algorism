import sys
from collections import deque

input = sys.stdin.readline

ans_list = []


def solve(n, tree, order) :

    visited = [False for i in range(n+1)]
    q = deque()

    q.append(1)
    visited[1] = True
    

    rank = [-1 for i in range(n+1)]

    for i in range(1,n+1) :
        rank[order[i-1]] = i 
    
    
    for i in range(1,n+1) :
        tree[i] = sorted(tree[i], key=lambda x : rank[x])

    while q :
        front = q.popleft()
        ans_list.append(front)

        for element in tree[front] :
            if visited[element] == False :
                visited[element] = True
                q.append(element)

    if ans_list == order :
        print(1)
    else :
        print(0)


n = int(input())
tree = [[] for _ in range(n+1)]

for _ in range(1,n) :
    x,y = map(int,input().split())
    tree[x].append(y)
    tree[y].append(x)

order = list(map(int,input().split()))


solve(n,tree,order)    