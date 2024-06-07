import sys

n = int(sys.stdin.readline()) #5

stack = []
str_reversed = []
command = []
#this is a test
#foobar
#all your base3

for i in range(n):
    command.append(sys.stdin.readline().strip()) 
    #['this is a test','foobar','all your base']
for index,str in enumerate(command):
    string_list = str.split() #'this','is', 'a', 'test'
    stack.extend(string_list)
    while stack:
        str_reversed.append(stack.pop())
    print("Case #{}: {}".format(index+1,' '.join(str_reversed)))  
    stack.clear()
    str_reversed.clear()           