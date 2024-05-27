n = list(map(int, list(input())))


def lucky(n):
    left = sum(n[0:len(n)//2])
    right = sum(n[(len(n)//2):])
    if left == right:
        print('LUCKY')
    else:
        print('READY')


if len(n):
    lucky(n)
else:
    print('READY')
