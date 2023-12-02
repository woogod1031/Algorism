n = int(input())

ropes = [] 

for _ in range(n):
  ropes.append(int(input()))
ropes.sort(reverse=True)
weight = ropes[0] # 50 40 10 10 10 10 10 10

for i in range(len(ropes)):
  weight = weight if weight >= ropes[i] * (i + 1) else ropes[i] * (i + 1)

print(weight)
  


