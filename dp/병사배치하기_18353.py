n = int(input())
array = list(map(int, input().split()))
array.reverse()

dp = [1] * n  # 병사 수

for i in range(1, n):
    for j in range(0, i):
        if array[i] > array[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
# 최장 증가 부분 수열(LIS) 알고리즘
# i번째 원소보다 작은 원소들의 dp값들 중 가장 큰 값 + 1

# 이미 이루어진 수열에 자기 자긴 값을 더해준다.
# 즉 작은 원소들의 dp값들(수열) 중 가장 큰 값 + 1
# i에 해당하는 값과 i 이전에 해당하는 값(j)들을 비교한다.

# 2와 4
# 5와 4, 2
# 8와 4, 2, 5
# 4와 4, 2, 5, 8
# 11와 4, 2, 5, 8, 4
# 15와 4, 2, 5, 8, 4, 11
