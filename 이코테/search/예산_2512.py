from sys import stdin 

input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))
total = int(input())


def binary_search(start, end, array, purpose):  
  if start > end:
    return end
  mid = (start + end)//2
  sum_value = 0
  for i in array:
    if i > mid:
      sum_value += mid
    else:
      sum_value += i

  if sum_value > purpose:
    end = mid - 1
  else:
    start = mid + 1
  
  return binary_search(start, end, array, purpose)

result = binary_search(0, max(arr), arr, total)
print(result)


