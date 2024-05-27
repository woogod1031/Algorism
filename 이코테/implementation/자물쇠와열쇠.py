def rotate(key):
    return list(zip(*key[::-1]))
# now = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]

# now90 = [[0, 1, 0], [1, 0, 0], [1, 0, 0]]

# now180 = [[1, 1, 0], [0, 0, 1], [0, 0, 0]]

# now270 = [[0, 0, 1], [0, 0, 1], [0, 1, 0]]


def attach(x, y, M, key, board):
    for i in range(M):
        for j in range(M):
            board[x+i][y+j] += key[i][j]


def detach(x, y, M, key, board):
    for i in range(M):
        for j in range(M):
            board[x+i][y+j] -= key[i][j]


def check(board, M, N):
    for i in range(N):
        for j in range(N):
            if board[M+i][M+j] != 1:
                return False
    return True


def solution(key, lock):
    M, N = len(key), len(lock)
    board = [[0] * ((M * 2) + N) for _ in range((M * 2) + N)]
    for i in range(N):
        for j in range(N):
            board[M+i][M+j] = lock[i][j]

    rotated_key = key

    # for _ in range(4):
    #     rotated_key = rotate(rotated_key)
    #     for x in range(1, M + N):
    #         for y in range(1, M + N):
    #             # 열쇠 넣어보기
    #             for i in range(M):
    #                 for j in range(M):
    #                     board[x + i][y + j] += rotated_key[i][j]
    #             # lock 가능 check
    #             if (check(board, M, N)):
    #                 return True
    #             # 열쇠 빼기
    #             for i in range(M):
    #                 for j in range(M):
    #                     board[x + i][y + j] -= rotated_key[i][j]

    for _ in range(4):
        rotated_key = rotate(rotated_key)
        for x in range(1, M+N):
            for y in range(1, M+N):
                # 열쇠 넣어보기
                for i in range(M):
                    for j in range(M):
                        board[x+i][y+j] += rotated_key[i][j]
                # lock 가능 check
                if check(board, M, N):
                    return True
                # 열쇠 빼기
                for i in range(M):
                    for j in range(M):
                        board[x+i][y+j] -= rotated_key[i][j]

    return False

# solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])
