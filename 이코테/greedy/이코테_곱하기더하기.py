n = list(map(int, list(input())))
n.sort()

result = 0

for i in n:
    if i <= 1 or result <= 1:
        result += i
    else:
        result *= i

print(result)
