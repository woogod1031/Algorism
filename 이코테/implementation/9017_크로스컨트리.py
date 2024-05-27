from sys import stdin

t = int(stdin.readline())
results = []

for _ in range(t):
  n = int(stdin.readline())
  temp = list(map(int, stdin.readline().split()))
  count = {}
  dele = {}
  team = {}

  for i in range(n):
    if temp[i] in count:
      count[temp[i]] += 1
    else:
      count[temp[i]] = 1    

  for k, v in count.items():
    if v < 6:
      dele[k] = 1
  
  idx = 1
  for i in range(n):
    if temp[i] not in dele:
      if temp[i] in team:
        if team[temp[i]][0] < 4:
          team[temp[i]][0] += 1
          team[temp[i]][1] += idx
        elif team[temp[i]][0] == 4:
          team[temp[i]][0] += 1
          team[temp[i]][2] = idx
      else:
        team[temp[i]] = [1, idx, 0]            
      idx += 1  
  team = sorted(team.items(), key = lambda x:(x[1][1], x[1][2])) 
  results.append(team[0][0])

for i in results:
  print(i)
  