n = int(input())
li = list(map(int, input().split()))
li.sort()

result = 100000

for i in range(1, li[-1] + 1):
    temp = 0
    for j in li:
        temp += abs(i - j)
    result = min(result, temp)

print(result)
