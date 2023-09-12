from sys import stdin

n, m = list(map(int, stdin.readline().split()))
result = 0

for i in range(n):
  num = min(list(map(int, stdin.readline().split())))
  min_value = min(num)
  result = max(result, min_value)
print(result)
