from itertools import combinations

n, m = map(int, input().split())

house, chicken = [], []
for i in range(n):
    li = list(map(int, input().split()))
    for j in range(n):
        if li[i][j] == 1:
            house.append((i, j))
        elif li[i][j] == 2:
            chicken.append((i, j))

result = int(1e9)

all_combination = combinations(chicken, m)


def get_distance(combi):
    result = 0
    for hou in house:
        x, y = hou
        temp = int(1e9)
        for com in combi:
            cx, cy = com
            temp = min(temp, abs(x - cx) + abs(y - cy))
        result += temp
    return result


for combi in all_combination:
    result = min(result, get_distance(combi))

print(result)
