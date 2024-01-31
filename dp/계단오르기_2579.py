# 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다.
# 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
# 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
# 마지막 도착 계단은 반드시 밟아야 한다.

n = int(input())
data = [0]
for _ in range(n):
    data.append(int(input()))

dp = [0] * (n + 1)

if n <= 2:
    print(sum(data))
else:
    dp[1] = data[1]
    dp[2] = data[1] + data[2]
    for i in range(3, n + 1):
        dp[i] = max(data[i] + data[i-1] + dp[i-3], data[i] + dp[i-2])

    print(dp[-1])
