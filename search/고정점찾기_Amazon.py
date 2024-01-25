n = int(input())
arr = list(map(int, input().split()))


def solution(start, end):
    if start > end:
        return -1
    mid = (start + end)//2
    if arr[mid] == mid:
        return mid
    if arr[mid] > mid:
        return solution(0, mid - 1)
    else:
        return solution(mid + 1, end)


print(solution(0, n - 1))
