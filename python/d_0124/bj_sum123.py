import sys
T = int(sys.stdin.readline()) #3
n = []
result = []

for _ in range(T):
    n.append(sys.stdin.readline()) #4,7,9

for num in n: #4,7,9
    count = 0

    def backtrack(value, sum):

        global count        

        if sum >= int(num):
            return
        sum += value
        if sum == int(num):
            count += 1
        backtrack(1,sum) #(1,1,1,1),(1,1,2),(1,2,1),(1,3)
        backtrack(2,sum) #(2,1,1),(2,2)
        backtrack(3,sum) #(3,1)

    backtrack(0,0)
    print(count)



