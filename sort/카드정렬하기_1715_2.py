import heapq

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort()
total = 0
for i in range(n - 1):
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)

    c = a + b
    total += c
    heapq.heappush(arr, c)

print(total)
