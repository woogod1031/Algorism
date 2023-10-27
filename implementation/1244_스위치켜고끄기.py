from sys import stdin

s_count = int(stdin.readline())
s_list = list(map(int, stdin.readline().split()))
switch = {}

for i in range(len(s_list)):
  switch[i + 1] = s_list[i]

stu_count = int(stdin.readline())

def change(v):
  global switch
  switch[v] = 0 if switch[v] == 1 else 1  

def multiples(n):
  global switch
  multiple = [x for x in range(n, s_count + 1, n)]
  for ix in multiple:
    change(ix)

def calcul(n):  
  change(n)
  for ix in range(1, s_count - n + 1):
    if n + ix in switch and n - ix in switch and switch[n + ix] == switch[n - ix]:
      change(n + ix)  
      change(n - ix)        
    else:
      break;      

for _ in range(stu_count):
  sex, num = list(map(int, stdin.readline().split()))
  if(sex == 1):
    multiples(num)
  else:
    calcul(num)

for k in range(1,s_count+1):
  print(switch[k], end=" ")
  if k%20 == 0:
    print()
