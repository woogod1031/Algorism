n = list(map(int, list(input())))

count = [0, 0]


def counting():
    now = n[0]
    for i in n:
        if now == i:
            continue
        else:
            count[now] += 1
            now = i
    count[now] += 1


def oper():
    if count[0] == len(n) or count[1] == len(n):
        return print(0)
    if count[1] >= count[0]:
        return print(count[0])
    else:
        return print(count[1])


counting()
oper()
