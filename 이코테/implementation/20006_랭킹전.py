from sys import stdin

p, m = list(map(int, stdin.readline().split()))
room = []

def create(level, nickname):
  global room
  room.append([{ 'nickname': nickname, 'level': level}])

def join(level, nickname):
  global room
  if len(room):
    for i in range(len(room)):
      if (len(room[i]) < m and room[i][0]['level'] + 10 >= level and room[i][0]['level'] - 10 <= level):
        room[i].append({
          'nickname': nickname,
          'level': level
        })
        break
      else:
        if(i + 1 == len(room)):
          create(level, nickname)
  else:
    create(level, nickname)

for _ in range(p):
  l, n = stdin.readline().split()
  l = int(l)
  join(l, n)

for j in range(len(room)):
  result = sorted(room[j], key = lambda x:x['nickname'])
  if len(result) == m:
      print('Started!')
      for k in result:
        print(k['level'], k['nickname'])
  else:
    print('Waiting!')    
    for l in result:
        print(l['level'], l['nickname'])
