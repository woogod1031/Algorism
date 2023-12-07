n = int(input())
arr = []

for _ in range(n):
  name, score = input().split()
  int(score)
  arr.append((name, int(score)))

def sort_key(val):
  return val[1]

result = sorted(arr, key=sort_key)

for x in list(map(lambda x: x[0] ,result)):
  print(x, end=' ')