# def solution(food_times, k):  # [3,1,2] #k = 5초 네트워크 장애
#     time = 0
#     target = 0

#     while True:
#         if time == k:
#             return target + 1
#         if sum(food_times) == 0:
#             return -1
#         if food_times[target] == 0:
#             if target + 1 == len(food_times):
#                 target = 0
#             else:
#                 target += 1
#         else:
#             food_times[target] -= 1
#             time += 1
#             if target + 1 == len(food_times):
#                 target = 0
#             else:
#                 target += 1


# solution([3, 1, 2], 5)

import heapq


def solution(food_times, k):  # [3,1,2] #k = 5초 네트워크 장애
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))
    # [(1, 6), (1, 2), (3, 3), (4, 1), (5, 7), (6, 4), (7, 5), (8, 8)]

    need_time = 0
    prev_time = 0
    lenth = len(food_times)

    # 여기서 q배열은 작은 시간 순서인데 정확한 위치가 아닌 lenth를 바로 곱해도 되는 이유는?

    # 각 위치를 따져보면 처음값은 length - 위치가 되고 마지막 값은 length 값이 된다.
    # 예를들어 8,4,6 순서일때 각 위치에서 소요되는 시간은 (3x1) - 2 = 1초, (3x1) - 1 = 2초, (3x1) - 0 = 3초가 되지만
    # 한 턴을 도는데 각 위치랑 상관없이 최종적으로 3초가 소요되기때문에 length를 곱해줄 수 있다.
    while need_time + ((q[0][0] - prev_time) * lenth) <= k:
        now = heapq.heappop(q)[0]
        need_time += (now - prev_time) * lenth
        prev_time = now
        lenth -= 1

    result = sorted(q, key=lambda x: x[1])
    return result[(k - need_time) % lenth][1]


print(solution([4, 1, 3, 6, 7, 1, 5, 8], 27))


# 예를 들어 solution([8, 4, 6], 15)이 실행되면
# 3개의 음식을 4초동안인 12초를 실행해야 2번째 음식이 0이 되고
# [(8,1), (4,2), (6,3)] 은 [(4,1), (0,2), (2,3)]가 되고 [(4,1), (2,3)] 와 같아진다.
# 그리고 [(4,1), (2,3)] 이 둘 중에서 남은 3초(15초 - 12초)동안 먹방을 진행하고 중지되면
# 3번 차례에 멈춘 걸 알 수 있다.
