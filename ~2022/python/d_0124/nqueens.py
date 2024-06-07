import sys
sys.setrecursionlimit(10000)


def nqueen(n): #4

    visited = [0] * n 
    cnt = 0
    
    def dfs(row):

        def is_ok_on(nth_row): #0
            #현재 (row,col)에 위치한 노드가 다른 규칙에 어긋나지않는지 
            for rows in range(nth_row): #현재 row              
                if visited[nth_row] == visited[rows] or\
                 nth_row - rows == abs(visited[nth_row] - visited[rows]):
                    return False
            return True

        if row >= n: #n행까지 끝난경우 , 백트레킹 용
            # nonlocal 은 지역변수가 아님을 의미한다.
            nonlocal cnt
            cnt += 1          
            return 
      
        for col in range(n): #0행부터 3행까지  len => 4
            visited[row] = col #visited[0] = 0부터 => (0,0)->체크->(0,1)->체크->(0,2)...
            if is_ok_on(row): #if is_ok_on가 true면 다음 row로, false면 다음 col로
                dfs(row + 1)
    
    # 0번째 행에 퀸을 둔다.
    dfs(0) #0행부터 dfs시작
    return cnt

test = int(sys.stdin.readline()) #8
print(nqueen(test)) #nqueen(8)