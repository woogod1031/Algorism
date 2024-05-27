n = int(input())
array = list(map(int, input().split()))
array.sort()
m = int(input())
x = list(map(int, input().split()))



for i in x:
  result = None
  start = 0
  end = n - 1
  while start <= end:
    mid = (start + end)//2
    if array[mid] == i:
      result = mid
      break
    elif array[mid] > i:
      end = mid - 1
    else:
      start = mid + 1
      
  if result != None:
    print('yes', end=' ')
  else:
    print('no', end=' ')


# for i in x:
#   if i in array:
#     print('yes', end=' ')
#   else:
#     print('no', end=' ')