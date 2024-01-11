n = int(input())
m = list(map(int, input().split()))
m.sort()

target = 1

for i in m:
    # target을 만들 수 있는 조건
    # target보다 작거나 target과 값이 같아야 한다.
    if target < i:
        break
    else:
        target += i

print(target)

# 1 1 3 5  7  9
# 1 2 5 10 17 26
# 2 3 6 11 18 27

# 1 3 5  7  9
# 1
# 2
