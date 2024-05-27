# 생성할 원소 개수와 찾을 문자열
input_data = input().split()
n = int(input_data[0])
target = input_data[1]

# n개만큼 문자열 입력 
array = input().split()

def sequential_search(num, tar, arr):
  for i in range(num):
    if arr[i] == tar:
      return i + 1


result = sequential_search(n, target, array)