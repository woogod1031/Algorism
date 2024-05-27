n = int(input())
arr = list(map(int, input().split()))
start = list[0]
end = list[n - 1]


def solution(start, end):
    if start > end:
        return -1
    mid = (start + end)//2
    if arr[mid] == mid:
        return mid
    if mid > arr[mid]:
        return solution(mid + 1, end)
    else:
        return solution(start, mid - 1)


solution(start, end)
