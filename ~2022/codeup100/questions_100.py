# id:ktkwhms3

# variable = input()
# print(variable)

# c = int(ord(input())) + 1
# print(chr(c)) 

# a,b = list(map(float, input().split()))
# c = a * b
# print(c)

# n = input()
# s = input()
# print(int(n)*s)

# a,b = list(map(float, input().split()))
# c = a ** b
# print(c)

# a, b, c = list(map(int, input().split()))
# print(a+b+c, end=' ')
# print(format((a+b+c)/3, '.2f'))

# a = int(input())
# print(a<<1)

# a, b = list(map(int, input().split()))
# print(a << b)

# a, b = list(map(int, input().split()))
# print(a != b)

# a = int(input())
# print(a != 0)

# a, b = list(map(int, input().split()))
# print((not bool(a)) and (not bool(b)))

# print(a&b)
# 실제로 이 계산은 네트워크에 연결되어 있는 두 개의 컴퓨터가 데이터를 주고받기 위해
# 같은 네트워크에 있는지 아닌지를 판단하는데 사용된다.


# a, b = map(int, input().split())
# print(a ^ b)
# 두 장의 이미지가 겹쳐졌을 때 색이 서로 다른 부분만 처리할 수 있다.
# 배경이 되는 그림과 배경 위에서 움직이는 그림이 있을 때,
# 두 그림에서 차이만 골라내 배경 위에서 움직이는 그림의 색으로 바꿔주면
# 전체 그림을 구성하는 모든 점들의 색을 다시 계산해 입히지 않고
# 보다 효과적으로 그림을 처리할 수 있게 되는 것이다.
# 비행기 슈팅게임 등을 상상해보면 된다.

# n = int(input())

# if n>=90 :
#   print('A')
# else :
#   if n>=70 :
#     print('B')
#   else :
#     if n>=40 :
#       print('C')
#     else :
#       print('D')

# evaluate = {
#   'A' : 'best!!!',
#   'B' : 'good!!',
#   'C' : 'run!',
#   'D' : 'slowly~'
# } 
# n = input()
# print(evaluate[n] if n in evaluate else 'what?')

# m = int(input())
# v = m//3

# if v==1:
#   print('spring')
# elif v==2:
#   print('summer')
# elif v==3:
#   print('fall')
# else:
#   print('winter')

# n = int(input())

# while True:
#   n -= 1
#   print(n)
#   if n == 0:
#     break

# c = int(input())
# n = 0
# while n<=c :
#   print(n)
#   n+=1

# n = int(input())
# a= 0
# for i in range(n+1) :
#   if i%2==0:
#     a+=i
# print(a)

# d = int(input())
# n=0
# sum=0
# while True:  
#   n += 1
#   sum += n
#   if d <= sum:
#     print(n)
#     break

# a, b = list(map(int, input().split()))
# for i in range(1, a+1) :
#   for j in range(1, b+1) :
#     print(i, j)
    
# a = int(input(), 16)
# for i in range(1, 16):
#   print('%X'%a, '*%X'%i, '=%X'%(a*i), sep='')

# a = int(input())
# for i in range(1, a + 1):
#   print('X' if i%10==3 or i%10==6 or i%10==9 else i, end=' ')

# r,g,b = list(map(int, input().split()))
# n=0
# for i in range(r):
#   for j in range(g):
#     for k in range(b):
#       print(i, j, k)
#       n+=1
# print(n)

# 1초 동안 마이크로 소리강약을 체크하는 횟수를 h
# (헤르쯔, Hz 는 1초에 몇 번? 체크하는가를 의미한다.)

# 한 번 체크한 값을 저장할 때 사용하는 비트수를 b
# (2비트를 사용하면 0 또는 1 두 가지, 16비트를 사용하면 65536가지..)

# 좌우 등 소리를 저장할 트랙 개수인 채널 개수를 c
# (모노는 1개, 스테레오는 2개의 트랙으로 저장함을 의미한다.)

# 녹음할 시간(초) s가 주어질 때,

# 필요한 저장 용량을 계산하는 프로그램을 작성해보자.

# 실제로, 일반적인 CD 음질(44.1KHz, 16bit, 스테레오)로 1초 동안 저장하려면
# 44100 * 16 * 2 * 1 bit의 저장공간이 필요한데,
# 44100*16*2*1/8/1024/1024 로 계산하면 약 0.168 MB 정도가 필요하다.

# 이렇게 녹음하는 방식을 PCM(Pulse Code Modulation) 방법이라고 하는데,
# 압축하지 않은 순수한(raw) 소리 데이터 파일은 대표적으로 *.wav 가 있다.

# h,b,c,s = list(map(int, input().split()))
# print(format((h*b*c*s)/(1<<23), '.1f'), 'MB')

# w,h,b = list(map(int, input().split()))
# print(format((w*h*b)/(1<<23), '.2f'), 'MB')

# a = int(input())
# n=0
# sum=0
# while True :
#   sum+=n
#   n += 1
#   if sum>=a :
#     break
# print(sum)

# a = int(input())
# for i in range(1, a+1) :
#   if i%3==0:
#     continue
#   print(i, end=' ')


# a,d,n = list(map(int, input().split()))
# print(a + (d * (n-1)))

# a,d,n = list(map(int, input().split()))
# print(a * (d ** (n-1)))

# a,m,d,n = list(map(int, input().split()))
# sum=a
# for _ in range(n-1):
#   sum = (sum * m) + d

# print(sum)

# d = 1
# a,b,c = list(map(int, input().split()))
# while d%a!=0 or d%b!=0 or d%c!=0:
#   d+=1
# print(d)

# n = int(input())
# a = list(map(int,input().split()))

# for _ in range(len(a)):
#   print(a.pop(), end=' ')

# n = int(input())
# a = list(map(int,input().split()))
# min = a[0]
# for i in range(len(a)):
#   min = a[i] if min >= a[i] else min
# print(min)

# n = int(input())
# field = [[0 for _ in range(19)] for __ in range(19)]
# for _ in range(n):
#   x,y = list(map(int,input().split()))
#   field[x-1][y-1] = 1

# for i in field:
#   for j in i:
#     print(j, end=' ')
#   print()

# field = []
# for _ in range(19):
#    field.append(list(map(int,input().split())))
# n = int(input())

# for _ in range(n):
#   x,y = list(map(int,input().split()))
#   for i in range(19):
#     field[x-1][i] = 1 if field[x-1][i] == 0 else 0    
#   for j in range(19):
#     field[j][y-1] = 1 if field[j][y-1] == 0 else 0    

# for m in field:
#   for k in m:
#     print(k, end=' ')
#   print()


# h,w = list(map(int, input().split()))
# field = [[0 for _ in range(w)] for __ in range(h)]
# n = int(input())
# for ___ in range(n):
#   i,d,x,y = list(map(int,input().split()))
#   if d == 0:
#     for j in range(i):
#       field[x-1][y+j-1] = 1
#   else:
#     for j in range(i):
#       field[x+j-1][y-1] = 1

# for m in field:
#   for k in m:
#     print(k, end=' ')
#   print()

# field = [[00000][00000][00000][00000][00000]]

field = []
for _ in range(10):
   field.append(list(map(int,input().split())))
current = [1,1]
field[current[0]][current[1]] = 9

while True:    
  if field[current[0]][current[1] + 1] == 1 and field[current[0] + 1][current[1]] == 1:
    break  
  if field[current[0]][current[1]+1] in [0,2]:
    if field[current[0]][current[1]+1] == 0:
      field[current[0]][current[1]+1] = 9
      current = [current[0], current[1]+ 1]
      continue
    else:
      field[current[0] ][current[1]+ 1] = 9
      break      
  else:
    if field[current[0]+ 1][current[1]] == 0:
      field[current[0]+ 1][current[1]] = 9
      current = [current[0] + 1, current[1]]
      continue
    else:
      field[current[0] + 1][current[1]] = 9
      break 

for m in field:
  for k in m:
    print(k, end=' ')
  print()