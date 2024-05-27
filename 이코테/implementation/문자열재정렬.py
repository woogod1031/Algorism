n = input()
alpha = []
num = 0
for i in range(len(n)):
    if n[i].isdigit():
        num += int(n[i])
    else:
        alpha.append(n[i])

alpha.sort()

if num != 0:
    alpha.append(str(num))

print(''.join(alpha))
