import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
arr = []
char = []

for _ in range(n):
  c,s = input().split()
  if arr and arr[-1][1] == int(s):
    continue
  arr.append((c, int(s)))
sorted(arr, key=lambda x:x[1])


def search(start, end, array, val):      
  while start <= end:
    mid = (start + end)//2
    if val == array[mid][1]:
      return print(array[mid][0])
    elif val > array[mid][1]:
      start = mid + 1
    else:
      end = mid - 1
  print(array[end + 1][0])

for _ in range(m):
  x = int(input())
  search(0, len(arr) - 1, arr, x)