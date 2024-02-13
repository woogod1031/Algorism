import bisect

N = int(input())  # (1 ≤ N ≤ 2,000)
li = list(map(int, input().split()))  # <= 10,000,000
li.reverse()
# 4 2 5 8 4 11 15
# 2 5 8
arr = [li[0]]
# 하위 시퀀스의 요소가 오름차순으로 정렬되고
# 하위 시퀀스가 ​​가능한 한 긴 하위 시퀀스를 찾는 것을 목표로 한다.
# 이 하위 시퀀스는 반드시 연속적이거나 고유할 필요는 없다.

# 오름차순을 갖는다는 건
# 좌측엔 최대한 작은 값들로 순서를 유지시켜야한다.
for i in range(1, N):
    num = li[i]
    # list에 num이 이분탐색으로 들어갈 위치 리턴
    # bisect_left : 같은 값 있으면 왼쪽(index작은 쪽)에 위치하도록 이분 탐색
    idx = bisect.bisect_left(arr, num)
    if idx < len(arr):
        arr[idx] = num
    else:
        arr.append(num)

print(N - len(arr))
