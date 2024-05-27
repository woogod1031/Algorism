def solution(today, terms, privacies):
    d = {}
    answer = []
    todayArr = today.split('.')
    t_year = int(todayArr[0]) * 336
    t_month = int(todayArr[1]) * 28
    t_day = int(todayArr[2])
    total = t_year + t_month + t_day
    for term in terms:
        n, m = term.split()
        d[n] = int(m)*28

    for privacyIdx in range(len(privacies)):      
      target = privacies[privacyIdx].split()
      targetDate = target[0].split('.')
      targetAdd = target[1]

      if (total - ((int(targetDate[0]) * 336) + (int(targetDate[1]) * 28 ) + int(targetDate[2]) + d[targetAdd]) < 0):
        continue
      answer.append(privacyIdx + 1)
         
    return answer