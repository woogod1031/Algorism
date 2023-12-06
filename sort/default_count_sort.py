arr = list(map(int, input().split))

cnt = [0] * (max(arr) + 1)

for i in range(len(arr)):
  cnt[arr[i]] += 1

for i in range(len(cnt)):
  for j in range(cnt[i]):
    print(i, end=' ')