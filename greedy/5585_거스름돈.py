from sys import stdin

n = 1000 - int(stdin.readline()) # 80
li = [500, 100, 50, 10, 5, 1]
res = 0 
idx = 0

while n != 0:  
  res += n//int(li[idx])
  n = n%li[idx]    
  idx += 1  

print(res)

