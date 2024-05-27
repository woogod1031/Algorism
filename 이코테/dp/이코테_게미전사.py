n = int(input())
arr = list(map(int, input().split()))
a = [0] * (n + 1)

a[1] = arr[0]
a[2] = max(arr[0], arr[1])

for i in range(3, n + 1):
  a[i] = max(a[i - 1], a[i - 2] + arr[i-1])

print(a[n])