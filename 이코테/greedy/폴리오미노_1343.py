board = input()

result = ''
stack = []

def check():    
  global result, stack
  div1 = len(stack) // 4
  result += 'AAAA' * div1
  div2 = (len(stack) - (div1*4)) // 2
  result += 'BB' * div2
  stack = []

for i in range(len(board)):  
  if board[i] =='X':
    stack.append(board[i])
  else:      
    if len(stack)%2 == 1:
      result = -1
      break
    check()
    result+= '.'

  if len(board) == i + 1:    
    if len(stack)%2 == 1:
      result = -1      
    else:      
      check()        

print(result)

# board = input()

# board = board.replace('XXXX', 'AAAA')
# board = board.replace('XX', 'BB')

# if 'X' in board: print(-1)
# else: print(board)