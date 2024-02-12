original_string = list(input())
new_string = list(input())

ori_len = len(original_string) + 1
new_len = len(new_string) + 1

dp = [[5000] * (len(ori_len) + 1) for _ in range(new_len)]

dp[0][0] = 0

for i in range(1, new_len):
    dp[0][i] = i

for i in range(1, ori_len):
    dp[i][0] = i

for i in range(1, ori_len):
    for j in range(1, new_len):
        if original_string[i-1] == new_string[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1


print(dp[new_len - 1][ori_len - 1])

# 문자가 같으면 => 추가될 연산이 없다.
# 문자가 다르면 => 더하거나, 빼거나, 교체하거나

# 더하거나 => dp[i-1][j] + 1
# 빼거나 => dp[i][j-1] + 1
# 교체하거나 => dp[i-1][j-1] + 1

#    s a y
# s  0 1 2  s 빼 빼
# a  1 0 1  더 s 빼
# y  2 1 1  더 더 교
# d  3 2 2  더 더 교
# y  4 3
# y
