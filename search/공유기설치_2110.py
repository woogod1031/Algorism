import sys
input = sys.stdin.readline

n, c = map(int, input().split())
house = []
for _ in range(n):
    house.append(int(input()))
house.sort()
최소간격, 최대간격 = 1, house[-1] - house[0]
# 집 사이의 최소 거리, 최대 거리
result = 0

if c == 2:
    print(최대간격)
    # 집이 2개라면 무조건 처음, 마지막 집 사이의 거리
else:
    while 최소간격 < 최대간격:
        중간간격 = (최소간격 + 최대간격)//2

        temp_count = 1
        current = house[0]  # 맨 좌측에 하나 설치하고 시작

        for i in range(n):
            if house[i]-current >= 중간간격:
                temp_count += 1
                current = house[i]
        if temp_count >= c:  # 간격이 좁아 공유기를 너무 많이 설치함 => 간격을 넓힌다.
            result = 중간간격
            최소간격 = 중간간격 + 1
        elif temp_count < c:  # 간격이 넓어 공유기를 목표 수보다 적게 설치함 => 간격을 좁힌다.
            최대간격 = 중간간격
    print(result)
