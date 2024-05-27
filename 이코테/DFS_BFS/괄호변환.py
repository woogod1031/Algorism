def 올바른문자열(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
    return True


def 균형잡힌문자열(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i


def solution(p):
    if p == '':
        return ''
    answer = ''
    index = 균형잡힌문자열(p)
    u = p[:index + 1]
    v = p[index + 1:]
    if 올바른문자열(u):
        answer = u + solution(v)
    else:
        answer = '(' + solution(v) + ')'
        li = list(u[1:-1])
        for i in li:
            if i == '(':
                answer += ')'
            else:
                answer += '('

    return answer


print(solution(")("))
