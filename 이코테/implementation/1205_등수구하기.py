from sys import stdin

n, n_score, p = list(map(int, stdin.readline().split()))

ranks = []
if n != 0:
  ranks = list(map(int, stdin.readline().split()))
else:
  ranks = []
ranks.sort(reverse=True) 
array = ranks[:p] # 10 5 3 2 1 0  * * *

result = None

if len(array):
  for i in range(len(array)):
    cur = i + 1
    if array[i] == n_score:
      if len(ranks) >= p and array[-1] == array[i]:
        result = -1                
        break
      else:
        result = cur
        break
    elif array[i] < n_score:
      result = cur
      break
    else:
      if p <= i + 1:
        result = -1
        break
      elif len(array) == i + 1:
        result = cur + 1
        break
      else:
        continue
else:
  result = 1

print(result)