n = int(input())
data = [(0, 0)]
dp = [0] * (n + 2)

for _ in range(n):
    time, pay = map(int, input().split())
    data.append((time, pay))


def dp_f(x):
    if x == 0:
        return
    if x + data[x][0] - 1 > n:
        dp[x] = dp[x + 1]
    else:
        dp[x] = max(dp[x + 1], data[x][1] + dp[x + data[x][0]])
    dp_f(x - 1)


dp_f(n)

print(max(dp))
