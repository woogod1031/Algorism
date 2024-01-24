# (스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수) / (스테이지에 도달한 플레이어 수)
# 스테이지의 개수 N은 1 이상 500 이하의 자연수
# stages에는 1 이상 N + 1 이하의 자연수
# N + 1 은 마지막 스테이지(N 번째 스테이지) 까지 클리어 한 사용자

# 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열

def solution(N, stages):
    answer = []
    length = len(stages)
    stages.sort(reverse=True)  # [1, 2, 2, 2, 3, 3, 4, 6]

    total = length
    prev = 0

    for i in range(N):
        for j in range(length):
            if stages[j] > (i+1):
                prev += 1
            if stages[j] <= (i+1) or j == length - 1:
                if total == 0:
                    answer.append([0, i+1])
                else:
                    answer.append(((total-prev)/total, i + 1))
                total = prev
                prev = 0
                break

    answer.sort(key=lambda x: (-x[0], x[1]))
    return [i[1] for i in answer]


print(solution(2, [3]))
