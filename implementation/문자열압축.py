def solution(s):
    possible = len(s)//2
    answer = len(s)
    if len(s) <= 1:
        return 1
    for i in range(1, possible + 1):
        result = 0
        wait = s[:i]
        recycle = 1
        for j in range(i, len(s), i):
            now = s[j:j+i]
            if wait == now:
                recycle += 1
            else:  # 다르다면
                if recycle <= 1:  # 기존에 반복되던게 없다면
                    result += len(wait)
                    wait = now
                else:  # 기존에 반복되던게 있다면
                    result += len(wait) + len(str(recycle))
                    wait = now
                    recycle = 1

        if recycle <= 1:  # 기존에 반복되던게 남아있지 않다면
            result += len(wait)
        else:  # 기존에 반복되던게 남아있다면
            result += len(wait) + len(str(recycle))
        answer = min(answer, result)
    return answer


print(solution('aabbaccc'))
