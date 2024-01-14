from collections import deque

n = int(input())
graph = [[0]*(n+1) for _ in range(n+1)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

k = int(input())
apple = [[0]*(n+1) for _ in range(n+1)]
for _ in range(k):
    a, b = map(int, input().split())
    apple[a][b] = 2

l = int(input())
dirDict = dict()
for i in range(l):
    x, c = input().split()
    dirDict[int(x)] = c

queue = deque()

x, y = 1, 1
queue.append((x, y))
cnt = 0
direction = 0


def turn(alpha):
    global direction
    if alpha == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4


while True:
    cnt += 1
    x += dx[direction]
    y += dy[direction]
    if x < 1 or x >= n + 1 or y < 1 or y >= n + 1:
        break
    if apple[x][y] == 2:
        apple[x][y] = 0
        graph[x][y] = 1
        queue.append((x, y))
        if cnt in dirDict:
            turn(dirDict[cnt])
    elif apple[x][y] == 0 and graph[x][y] == 0:
        graph[x][y] = 1
        queue.append((x, y))
        tx, ty = queue.popleft()  # 꼬리빼기
        graph[tx][ty] = 0
        if cnt in dirDict:
            turn(dirDict[cnt])
    else:
        break

print(cnt)
