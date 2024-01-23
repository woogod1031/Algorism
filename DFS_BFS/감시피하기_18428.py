n = int(input())
graph = []

# 학생이 있다면 S
# 선생님이 있다면 T
# 아무것도 존재하지 않는다면 X
# 장애물은 O

for _ in range(n):
    graph.append(input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def 감시재귀(x, y, d):
    if x >= n or y >= n or x < 0 or y < 0 or graph[x][y] == 'O':
        return False
    if graph[x][y] == 'S':
        return True
    return 감시재귀(x + dx[d], y + dy[d], d)


def check():
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'T':
                # 모든 T가 S를 안 만나면 된다.
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 감시재귀(nx, ny, k):
                        return False
    return True


def solution(cnt):
    global graph

    if cnt == 3:
        if check():
            return True
        else:
            return False

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'X':
                cnt += 1
                graph[i][j] = 'O'
                if solution(cnt):
                    return True
                cnt -= 1
                graph[i][j] = 'X'
    return False


if solution(0):
    print('YES')
else:
    print('NO')
