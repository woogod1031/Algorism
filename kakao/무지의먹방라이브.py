import heapq
# food_times 의 길이는 1 이상 200,000 이하이다.
# food_times 의 원소는 1 이상 100,000,000 이하의 자연수이다.
# k는 1 이상 2 x 10^13 이하의 자연수이다.


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    length = len(food_times)
    total = 0
    prev_time = 0

    # 다음 차례에도 k값이 살아있어야되기 때문에 <=을 사용한다.
    # k가 6이라면 6의 위치가 아닌 그 다음에 먹어야되는 7에 해당하는 위치를 알아야 하기 때문에
    while (total + ((q[0][0] - prev_time) * length)) <= k:
        now = heapq.heappop(q)[0]
        __what = (now - prev_time) * length
        total += __what
        prev_time = now
        length -= 1

    result = sorted(q, key=lambda x: x[1])
    return result[(k-total) % length][1]
