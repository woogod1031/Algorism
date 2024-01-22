# 편의 상 레스토랑의 정북 방향 지점을 0으로 나타내며,
# 취약 지점의 위치는 정북 방향 지점으로부터 시계 방향으로 떨어진 거리로 나타냅니다.
# 또, 친구들은 출발 지점부터 시계, 혹은 반시계 방향으로 외벽을 따라서만 이동합니다.

# solution(외벽의 길이, 취약지점의 위치가 담긴 배열, 각 친구가 1시간 동안 이동할 수 있는 거리):
from itertools import permutations

# weak = 1, 3, 4, 9, 10, 13, 15, 16, 21, 22
# 친구들 = [3, 5, 7]


def get_friends_count():
    return


def solution(n, weak, dist):
    # weak 길이 두배로 나열
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
    answer = len(dist) + 1
    # 인덱스 "0부터 끝" 부터 "끝에서 0"까지
    for start in range(length):  # start위치
        for friends in list(permutations(dist, len(dist))):  # 순열
            cnt = 1  # 투입 수
            # position은 해당 친구가 점검할 수 있는 마지막 위치로 weak[start]부터 friends[cnt - 1]까지를 말한다.
            position = weak[start] + friends[cnt - 1]  # 현재 위치
            for idx in range(start, start + length):  # 투입된 사람으로 다 먹을 수 있는지 체크
                # 투입된 친구가 점검할 수 있는 것보다(position) weak[idx]값이 더 크다는 건
                # 투입된 친구가 점검할 수 있는 위치는 넘어갔다는 것으로 다른 한 명이 더 투입 되어야 한다는 걸 의미한다.
                if position < weak[idx]:
                    cnt += 1  # 사람 추가
                    # 투입 인원 초과로 더이상 가능한 인원이 없으면
                    # 다른 순열로 계산을 한다.
                    if cnt > len(dist):
                        break
                    # 사람 추가 후 position을 재 변경해준다.
                    # position은 cnt올리기 전 weak[start]부터 friends[cnt - 1]까지를 구했지만
                    # friends[cnt - 1]값이 weak[idx]가 되고 새로운 friends[cnt - 1]값을 더해서 길이를 연장해준다.
                    position = weak[idx] + friends[cnt - 1]
            answer = min(answer, cnt)

    if answer > len(dist):
        return -1
    return answer


solution(12, [1, 5, 6, 10], [1, 2, 3, 4])
# solution(12, [1, 3, 4, 9, 10], [3, 5, 7])
