from sys import stdin

# 상근이 트럭 3대 
# 트럭 주차의 비용 계산
# 1분에 1대 추차 대당 A원
# 1분에 2대 추차 대당 B원
# 1분에 3대 추차 대당 C원

# //입력
# 5 3 1
# 1 6
# 3 5
# 2 8
# //출력
# 33

a, b, c = list(map(int, stdin.readline().split()))
arr = [0] * 100
price = 0

for _ in range(3):
  st, et = map(int,input().split())
  for point in range(st, et):
    arr[point]+=1

for num in arr:
  price += { 0:0, 1:1*a, 2:2*b, 3:3*c }[num]

print(price)

