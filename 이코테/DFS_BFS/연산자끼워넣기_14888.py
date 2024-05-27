import sys
from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))
cnt_li = list(map(int, input().split()))
cal_li = ['+'] * cnt_li[0] + ['-'] * cnt_li[1] + \
    ['x'] * cnt_li[2] + ['/'] * cnt_li[3]

candidates = list(set(permutations(cal_li, n-1)))

_max = -sys.maxsize
_min = sys.maxsize

for i in range(len(candidates)):
    val = arr[0]
    for j in range(n-1):
        if candidates[i][j] == '+':
            val += arr[j+1]
        elif candidates[i][j] == '-':
            val -= arr[j+1]
        elif candidates[i][j] == 'x':
            val *= arr[j+1]
        else:
            val = int(val / arr[j+1])
    if val >= _max:
        _max = val
    if val < _min:
        _min = val

print(_max)
print(_min)
