n = int(input())

a = [0] * (n + 1)

a[1] = 1
a[2] = 3

for i in range(3, n + 1):
  a[i] = (a[i-1] + 2 * a[i-2]) % 796796

print(a[n])
