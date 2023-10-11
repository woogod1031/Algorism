def solution(park, routes):    
    answer = []
    
    for i in range(len(park)):
      for j in range(len(park[i])):
        if (park[i][j] == 'S'):
          answer = [i, j]          
          break

    for route in routes:
      current = answer[:]  # 0, 1 => y, x
      cnt = 0
      if route[2] == 0:
        continue
      for step in range(int(route[2])):
        if route[0] == 'E' and current[1] + 1 != len(park[0]) and park[current[0]][current[1] + 1] != 'X':
         current[1] += 1 
         cnt += 1
        elif route[0] == 'W' and current[1] != 0 and park[current[0]][current[1] - 1] != 'X':
          current[1] -= 1 
          cnt += 1
        elif route[0] == 'S' and current[0] + 1 != len(park) and park[current[0] + 1][current[1]] != 'X':        
          current[0] += 1 
          cnt += 1
        elif route[0] == 'N' and current[0] != 0 and park[current[0] - 1][current[1]] != 'X':
          current[0] -= 1 
          cnt += 1
        else:
          break
      if cnt != int(route[2]):
        continue         
      answer = current[:]
    
    return answer