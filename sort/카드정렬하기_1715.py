import heapq
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort()

total = 0
for _ in range(n - 1):
    if len(arr) >= 2:
        a = heapq.heappop(arr)
        b = heapq.heappop(arr)
        value = a + b
        total += value
        heapq.heappush(arr, value)

print(total)
