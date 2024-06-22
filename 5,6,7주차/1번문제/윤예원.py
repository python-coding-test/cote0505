def solution(today, terms, privacies):
    y,m,d = today.split(".")
    todayCnt = int(y)*12*28+ int(m)*28+int(d)
    term_dict = {}
    for term in terms:
        type, period = term.split()
        term_dict[type] = int(period)
    result = []
    for i, privacy in enumerate(privacies):
        date, type = privacy.split()
        y1,m1,d1 = date.split(".")
        dateCnt = int(y1)*12*28+ int(m1)*28+int(d1)
        dateCnt += (term_dict[type]*28-1)
        if dateCnt < todayCnt:
            result.append(i+1)

    return result