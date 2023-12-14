n = int(input())

# obj = {}
array = [0]*n

# 하향식
def fibo(x):
  if x == 0 or x == 1:
    return 1
  # if x in obj:
  #   return obj[x]
  # else:
  #   obj[x] = fibo(x - 1) + fibo(x - 2)
  #   return obj[x]    
  if array[x] == 0:
    array[x] = fibo(x - 1) + fibo(x - 2)
    return array[x]
  else:
    return array[x]

print(fibo(n - 1))

#상향식

def pibo(x):
  array[0] = 1
  array[1] = 1
  for i in range(2, x):
    array[i] = array[i - 1] + array[i - 2]    

pibo(n)
print(array[n - 1])