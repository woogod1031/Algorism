class Solution(object):
    def solveNQueens(n):
        count = 0
        visited = [0] * n
        answers = []

        def dfs(row):

            def is_ok_on(nth_row):
                for rows in range(nth_row):  # 0,1,2
                    if visited[nth_row] == visited[rows] or\
                            nth_row - rows == abs(visited[nth_row] - visited[rows]):
                        return False
                return True

            if row >= n:
                nonlocal count
                count += 1
                grid = [['.'] * n for _ in range(n)]
                for idx, value in enumerate(visited):
                    grid[idx][value] = 'Q'
                result = []
                for row in grid:
                    print(row)
                    result.append(''.join(row))
                answers.append(result)
                return

            for col in range(n):
                visited[row] = col
                if is_ok_on(row):
                    dfs(row + 1)

        dfs(0)
        return answers
