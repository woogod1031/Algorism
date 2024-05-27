# 기둥은
#   바닥 위에 있거나
#   보의 한쪽 끝 부분 위에 있거나, 또는
#   다른 기둥 위에 있어야 합니다.

# 보는
#   한쪽 끝 부분이 기둥 위에 있거나, 또는
#   양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.

def check(result):
    for x, y, a in result:
        if a == 0:
            if y == 0 or [x - 1, y, 1] in result or [x, y, 1] in result or [x, y - 1, 0] in result:
                continue
            else:
                return False
        elif a == 1:
            if [x, y-1, 0] in result or [x + 1, y-1, 0] in result or ([x-1, y, 1] in result and [x+1, y, 1] in result):
                continue
            else:
                return False
    return True


# 쌓는 순서대로 진행 하고 return은 그 순서를 반환한다고 생각하면 될듯
def solution(n, build_frame):
    result = []

    for x, y, a, b in build_frame:
        item = [x, y, a]
        if b == 1:
            result.append(item)
            if not check(result):
                result.remove(item)
        elif item in result:
            result.remove(item)
            if not check(result):
                result.append(item)

    return sorted(result)


# print(solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [
#       1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))
