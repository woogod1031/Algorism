n, m = map(int, input().split())

a = list(map(int, input().split()))  # n개, 1 ~ m 까지
# cnt = 0

# for j in range(len(a)):
#     for k in range(len(a)):
#         if j == k:
#             continue
#         else:
#             if a[j] == a[k]:
#                 continue
#             else:
#                 cnt += 1

# print(cnt//2)

###

arr = [0] * 11

for i in a:
    arr[i] += 1

result = 0
# n은 개수
for i in range(1, m + 1):
    n -= arr[i]
    # i무개를 가진 공의 개수와 i무개를 제외한 남은 공의 개수의 곱
    result += arr[i] * n

print(result)
