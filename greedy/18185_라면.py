from sys import stdin

n = int(stdin.readline())
i = list(map(int, stdin.readline().split()))
cost = 0

def buy3 (idx):
  global cost
  if (j + 2 < n and i[idx + 2] != 0):        
      m2 = min(i[idx], i[idx + 1], i[idx + 2])
      i[idx] -= m2  
      i[idx + 1] -= m2
      i[idx + 2] -= m2
      cost += (7 * m2)

def buy2 (idx):
  global cost
  if (idx + 1 < n and i[idx + 1] != 0):                        
    m1 = min(i[idx], i[idx + 1])
    i[idx] -= m1  
    i[idx + 1] -= m1
    cost += (5 * m1)
    
def buy1 (idx):
  global cost
  if (i[idx] != 0):                  
    cost += 3 * i[idx]

for j in range(n):  
  if (j + 1 < n and j + 2 < n and i[j + 1] > i[j + 2]):
    m = min(i[j], i[j+1] - i[j+2])
    i[j] -= m
    i[j+1] -= m
    cost += 5*m
    buy3(j)
    buy1(j)    
  else:
    buy3(j)
    buy2(j)
    buy1(j)
    
print(cost)