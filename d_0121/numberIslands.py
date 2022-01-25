def island_dfs_stack(grid):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    rows, cols = len(grid), len(grid[0])
    cnt = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] != '1':
                continue

            cnt += 1
            stack = [(row, col)]

            while stack:
                x, y = stack.pop()
                grid[x][y] = '0'
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != '1':
                        continue
                    stack.append((nx, ny))
    return cnt
    

def island_dfs_recursive(grid):

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    cnt = 0

    def dfs_recursive(i, j):

        if (i < 0 or 
            i >= len(grid) or 
            j < 0 or 
            j >= len(grid[0]) or 
            grid[i][j] != '1'):

            return

        # 방문처리
        grid[i][j] = '0'
        for i in range(4):
            dfs_recursive(i + dx[i], j + dy[i])
        return


    for i in range(len(grid)):
        for j in range(len(grid[0])):
            node = grid[i][j]

            if node != '1': #1이 아니면 넘기기
                continue

            cnt += 1
            dfs_recursive(i, j)

    return cnt

def numIslands(grid):
    def dfs(i,j):
        if( i < 0 or i >= len(grid) or \
            j < 0 or j >= len(grid)[0] or \
            grid[i][j] != '1'):
            return
        
        grid[i][j] = 0

        dfs(i,j+1)
        dfs(i,j-1)
        dfs(i-1,j)
        dfs(i+1,j)  
        
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid(0))):
            if grid[i][j] == '1':
                dfs(i,j)
                count += 1
    
    return count




assert island_dfs_stack(grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]) == 1
assert island_dfs_stack(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]) == 3