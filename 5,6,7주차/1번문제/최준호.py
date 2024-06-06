def solution(today, terms, privacies):
    answer = []

    contract = {}
    for i in terms:
        t, m = i.split()
        contract[t] = int(m)

    YEAR = 12
    ty, tm, td = map(int, today.split('.'))

    for i, privacy in enumerate(privacies):
        days, t = privacy.split()
        y, m, d = map(int, days.split('.'))
        i += 1

        m = m + contract[t]
        while m > 12:
            y += 1
            m -= 12

        if y < ty:
            answer.append(i)

        elif y == ty and m < tm:
            answer.append(i)

        elif y ==ty and m == tm and d <= td:
            answer.append(i)

    answer.sort()
    return answer