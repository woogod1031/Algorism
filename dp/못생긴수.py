n = int(input())

ugly = [False] * 1001
ugly[1] = True

for i in range(2, 1001):
    if i % 2 == 0:
        ugly[i] = True
    elif i % 3 == 0:
        ugly[i] = True
    elif i % 5 == 0:
        ugly[i] = True

result = [i for i in range(1, 1001) if ugly[i] == True]

result[n]
