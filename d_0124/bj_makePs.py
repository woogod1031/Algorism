import sys

length, word = map(int,sys.stdin.readline().split())
#4,6
alphabet = list(map(str,sys.stdin.readline().split()))
#a,b,c,d,e,f
alphabet.sort()
visited = ['0'] * length
answer = []

def dfs(leng,index):
    if len == length:
        vo = 0
        co = 0
        for i in range(length):
            if visited[i] in 'aeiou':
                vo += 1


dfs(0,0)

