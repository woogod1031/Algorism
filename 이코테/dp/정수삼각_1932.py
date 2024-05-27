n = int(input())
dp = []
for _ in range(n):
    dp.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(len(dp[i])):
        left_top = 0
        right_top = 0
        if j == 0:
            left_top = 0
        else:
            left_top = dp[i - 1][j - 1]

        if j == len(dp[i]) - 1:
            right_top = 0
        else:
            right_top = dp[i - 1][j]

        dp[i][j] = dp[i][j] + max(left_top, right_top)

result = max(dp[n - 1])
print(result)
