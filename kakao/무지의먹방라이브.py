# food_times 의 길이는 1 이상 200,000 이하이다.
# food_times 의 원소는 1 이상 100,000,000 이하의 자연수이다.
# k는 1 이상 2 x 10^13 이하의 자연수이다.

def solution(food_times, k):
    cnt = 0
    while k != 0:
        if sum(food_times) == 0:
            return -1
        val = cnt % len(food_times)
        if food_times[val] != 0:
            food_times[val] -= 1
            cnt += 1
            k -= 1
        else:
            cnt += 1

    if sum(food_times) == 0:
        return -1
    for _ in range(len(food_times)):
        target = cnt % len(food_times)
        if food_times[target] != 0:
            return target + 1
        else:
            cnt += 1


print(solution([1, 100], 10))
