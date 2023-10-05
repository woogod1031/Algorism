from sys import stdin

n = int(stdin.readline())
l = list(map(int, stdin.readline().split()))
arr = [0] * n 

for i in range(n):
  count = l[i]
  for j in range(n):
    if (count == 0 and arr[j] == 0):
      arr[j] = i + 1            
      break
    if (arr[j] == 0):
      count -= 1

print(*arr)