import sys



def isParenthesis(str):

    stack = []
    table = {')':'('}
    opener = '('

    if len(str) % 2 != 0 or len(str) == 0:
        print('NO')
        return
        
    for n in str:
        if n == opener:
            stack.append(n)
        elif n == ')':
            if not stack:
                print('NO')
                return
            if table[n] != stack.pop():
                print('NO')
                return 
        else:
            print('NO')
            return 
    if not stack:
        print('YES')
    else:
        print('NO')           

n = int(sys.stdin.readline())

for i in range(n):
        command = sys.stdin.readline().split()
        isParenthesis(command[0])