from sys import stdin

h, w = list(map(int, stdin.readline().split()))
city = []

for _ in range(h):
  line = stdin.readline().replace('\n', '')
  city.append(list(line))

for i in range(h):
  for j in range(w):
    if city[i][j] == 'c':
      print(0, end=' ')  
    else:
      spice = city[i][:j]
      if 'c' in spice:   
        spice.reverse()
        target_index = len(spice) - 1 - spice.index('c')
        print(j - target_index, end=' ')
      else:
        print(-1, end=' ')      
  if h -1 > i:      
    print()