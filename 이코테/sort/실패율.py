# (스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수) / (스테이지에 도달한 플레이어 수)
# 스테이지의 개수 N은 1 이상 500 이하의 자연수
# stages에는 1 이상 N + 1 이하의 자연수
# N + 1 은 마지막 스테이지(N 번째 스테이지) 까지 클리어 한 사용자

# 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열

def solution(N, stages):
    answer = []
    length = len(stages)
    for i in range(1, N + 1):
        count = stages.count(i)
        if length == 0:
            fail = 0
        else:
            fail = count / length

        answer.append((i, fail))
        length -= count
    print(answer)
    answer.sort(key=lambda x: (-x[1], x[0]))
    return [i[0] for i in answer]


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
