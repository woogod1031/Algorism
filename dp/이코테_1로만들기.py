n = int(input())
arr = [0] * (n + 1)
# 각 인덱스에 해당하는 값들은 최소 연산 수를 뜻한다.

# 예를들어 arr[5]의 최소 연산이 2, arr[24]의 최소연산이 3일 때 arr[25]에 해당하는 값은
# 1. arr[24]의 최소 연산 수에 "+ 1" 연산을 한 값일 수도 있고 => 3 + 1
# 2. arr[5]의 최소 연산 수에 "x 5" 연산을 한 값일 수도 있다 => 2 + 1


arr[1] = 1

for i in range(2, n+1):
  arr[i] = arr[i - 1] + 1
  if arr[i] % 5 == 0:    
    arr[i] = min(arr[i], arr[i//5] + 1)
  if arr[i] % 3 == 0:    
    arr[i] = min(arr[i], arr[i//3] + 1)
  if arr[i] % 2 == 0:    
    arr[i] = min(arr[i], arr[i//2] + 1)
  
print(arr[n])


# 위 식을 사용해서 1을 만들때 최소 값을 구해라.

