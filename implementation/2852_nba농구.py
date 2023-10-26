from sys import stdin

total_goals = int(stdin.readline())
score = {1: 0, 2: 0}
time = {1: 0, 2: 0}
ans = {1: 0, 2: 0}
state = 0

def conversion(t):
  hr, mi = list(map(int, t.split(':')))
  return (hr * 60) + mi   

for _ in range(total_goals):
  team, t = stdin.readline().split()
  team = int(team)
  min = conversion(t)  
  score[team] += 1
  
  if state == 0:
    time[team] = min
    state = team
  elif state != 0 and score[1] == score[2]: 
    ans[state] += min-time[state]
    state = 0

if state != 0:
  ans[state] += (48 * 60)-time[state]

print('{:0>2}:{:0>2}'.format(ans[1]//60, ans[1] % 60))
print('{:0>2}:{:0>2}'.format(ans[2]//60, ans[2] % 60))
  
  

  