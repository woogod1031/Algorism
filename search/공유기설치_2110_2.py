import sys
input = sys.stdin.readline

n, c = map(int, input().split())
house = []

for _ in range(n):
    house.append(int(input()))
house.sort()

min_gap, max_gap = 1,  house[-1] - house[0]
if c == 2:
    print(max_gap)
else:
    result = 0
    while min_gap <= max_gap:
        mid_gap = (max_gap + min_gap) // 2
        cnt = 1
        current = house[0]
        for i in range(1, n):
            if house[i] - current >= mid_gap:
                cnt += 1
                current = house[i]
        if cnt < c:
            max_gap = mid_gap - 1
        elif cnt >= c:
            min_gap = mid_gap + 1
            result = mid_gap

    print(result)
