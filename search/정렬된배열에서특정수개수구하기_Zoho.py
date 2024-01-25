
n, x = map(int, input().split())
arr = list(map(int, input().split()))


def count_by_value(array, x):
    n = len(array)
    a = first(array, x, 0, n-1)
    if a == None:
        return 0
    b = last(array, x, 0, n - 1)

    return b - 1 + 1


def first(array, target, start, end):
    if start > end:
        return None
    mid = (start + end)//2

    if (mid == 0 or target > array[mid-1]) and array[mid] == target:
        return mid

    if array[mid] >= target:
        return first(array, target, start, mid - 1)
    else:
        return first(array, target, mid + 1, end)


def last(array, target, start, end):
    if start > end:
        return None
    mid = (start + end)//2

    if (mid == n - 1 or target < array[mid+1] and array[mid] == target):
        return mid
    elif array[mid] > target:
        return last(array, target, start, mid - 1)
    else:
        return last(array, target, mid + 1, end)


count = count_by_value(arr, x)

if count == 0:
    print(-1)
else:
    print(count)
