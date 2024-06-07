import sys

n = int(sys.stdin.readline())
stick = [int(sys.stdin.readline()) for _ in range(n)]
stack = []

if not stick:
    print(0)
else:
    for item in stick:
        while stack and item >= stack[-1]:
            stack.pop()            
        stack.append(item)

print(len(stack))
