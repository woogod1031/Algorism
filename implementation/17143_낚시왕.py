from sys import stdin

map_r, map_c, m = map(int, stdin.readline().split())
arr = [0] * m
total_shark_size = 0
for i in range(m):
  r, c, s, d, z = map(int, stdin.readline().split())
  arr[i] = {'id':i, 'r':r, 'c':c, 's':s, 'd':d, 'z':z }

for j in range(map_c):
  cur_column = j + 1    
  selcted_sharks = [n for n in arr if n['c'] == cur_column]  
  if len(selcted_sharks):
    target = max(selcted_sharks, key= lambda n: map_r - n['r'])        
    arr = [x for x in arr if x['id'] != target['id']]
    total_shark_size += target['z']
  result = []
  for idx in range(len(arr)):
    target = arr[idx].copy()
    if target['d'] == 1 or target['d'] == 2:
      cycle = map_r * 2 - 2
      current = 0                  
      if target['d'] == 1:
        current = (cycle - target['r'] + 2) + target['s']                
      else:
        current = target['r'] + target['s']                
      current %= cycle
      if current > map_r:
        target['r'] = cycle - current + 2
        target['d'] = 1
      elif current == 0:
        target['r'] = 2
        target['d'] = 1
      else:
        target['r'] = current
        target['d'] = 2      
    else: 
      cycle = map_c * 2 - 2
      current = 0
      if target['d'] == 3:
        current = target['c'] + target['s']                
      else:
        current = (cycle - target['c'] + 2) + target['s']                
      current %= cycle
      if current > map_c:
        target['c'] = cycle - current + 2
        target['d'] = 4     
      elif current == 0:
        target['c'] = 2
        target['d'] = 1 
      else:
        target['c'] = current
        target['d'] = 3   
           
    if len(result):
      for ix in range(len(result)):      
        if result[ix]['c'] == target['c'] and result[ix]['r'] == target['r']:
          if result[ix]['z'] > target['z']:
            break
          else:
            n_result = []            
            n_result = [v for v in result if v['id'] != result[ix]['id']]    
            n_result.append(target)            
            result = n_result            
            break    
        else:
          if ix + 1 == len(result):
            result.append(target)        
          else: continue
    else:
      result.append(target)         
  arr = result            
print(total_shark_size)  