import sys
input_data = sys.stdin.readline().rstrip()

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

# 재귀함수로 구현
def binary_search(arr, tar, start, end):
  if start > end:
    return None
  mid = (start + end)//2
  if arr[mid] == tar:
    return min
  elif arr[mid] > target:  # mid의 좌 우측 중 어디에 있는지 체크
    return binary_search(arr, tar, start, mid - 1)
  else:
    return binary_search(arr, tar, mid + 1, end)
  

result = binary_search(array, target, 0, n-1)

if result != None:
  print(result + 1)


# 단순 반복문으로 구현
n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

def binary_search(arr, tar, start, end):
  while start <= end:
    mid = (start + end)//2
    if arr[mid] == tar:
      return mid
    elif arr[mid] > tar:
      end = min - 1
    else: 
      start = mid + 1


result = binary_search(array, target, 0, n-1)
if result != None:
  print(result + 1)
