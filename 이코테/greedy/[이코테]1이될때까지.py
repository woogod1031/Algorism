from sys import stdin

n, k = list(map(int, stdin.readline().split()))
# 25 3
count = 0

while True: 
  count = count + (n % k)
  n = (n//k) * k
  if n < k:
    break
  n = n//k
  count = count + 1

count = count + (n - 1)
print(count)
# while n != 1:
#   if (n%k == 0):
#     n //= k
#   else:
#     n -= 1
#   num += 1