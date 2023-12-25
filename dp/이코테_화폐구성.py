import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

array = []
for i in range(n):
    array.append(int(sys.stdin.readline().rstrip()))

d = [10001] * (m + 1)

d[0] = 0
for i in range(n): #2 3 5
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001:
            d[j] = min(d[j], d[j - array[i]] + 1)
            # 이전에 계산 된 d[j] 값이랑 현재의 d[j - array[i] + 1] 값과 비교한다.

if d[m] == 10001:
    print(-1)
else:
    print(d[m])

