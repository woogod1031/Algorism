from sys import stdin

n, m, k = list(map(int, stdin.readline().split()))
li = sorted(list(map(int, stdin.readline().split())))

num1 = li[n - 1]
num2 = li[n - 2]
result = 0

share = int(m / (k+1))
remainder = int(m % (k + 1))

result += (num1 * k * share) + (num1 * remainder)
result += num2 * share

print(result)

# for i in range(1, m + 1):
#   if i%(k + 1) == 0:
#     result += num2
#   else:
#     result += num1