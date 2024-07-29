def solution(today, terms, privacies):
    answer = []
    
    def makeDays(time):
        year, month, day = map(int, time.split("."))
        return (year-1)*12*28 + month*28 + day
    
    today_days = makeDays(today)
    #print(f" {today} -> {today_days}일") # 2022.05.19 -> 679215일
    
    dict = {}
    for term in terms:
        types, period = term.split(" ")
        dict[types] = int(period)
    # print(f"dict : {dict}") # dict : {'A': 6, 'B': 12, 'C': 3}
    
    for idx, privacy in enumerate(privacies):
        start, types = privacy.split(" ")
        start_days = makeDays(start)
        #print(f" {start} -> {start_days}일")
        end_days = start_days + dict[types]*28
        if (end_days <= today_days):
            answer.append(idx+1)

    
    return answer