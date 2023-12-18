n = int(input())

a = [0] * (n + 1)

a[1] = 'SK'

for i in range(2, n + 1):
  a[i] = 'CY' if a[i - 1] == 'SK' else 'SK'
  if i - 3 > 0:
    a[i] = 'CY' if a[i - 3] == 'SK' else 'SK'

print(a[n])