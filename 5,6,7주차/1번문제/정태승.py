def solution(today, terms, privacies):
    answer = []
    
    te = {} # 약관 종류 : 보관기간
    pr = {} # (번호, 약관 종류) : 생성시간
    
    today_year, today_month, today_day = list(map(int, today.split('.')))
    
    for t in terms:
        a, b = t.split()
        te[a] = b
    
    for idx, p in enumerate(privacies):
        a, b = p.split()
        pr[(idx+1, b)] = a

    for k, v in pr.items():
        duration, created_at = int(te[k[1]]), pr[k]
        c = list(map(int, created_at.split('.')))
        year = c[0]
        month = c[1]
        day = c[2]
        
        
        if month + duration <= 12:
            month = month + duration
        else:
            add_year = (duration) // 12
            rest_month = (duration) % 12
            
            year += add_year
            
            if month + rest_month <= 12:
                month = month + rest_month
            else:
                year += (month+rest_month) // 12
                month = (month+rest_month) % 12
            
        
        if year < today_year: # 오늘이 파기년도를 지났다면 파기.
            answer.append(k[0])
        elif year==today_year and month < today_month: # 이번달이 파기달을 지났다면 파기
            answer.append(k[0])
        elif year==today_year and month==today_month and day <= today_day:
            answer.append(k[0])
        
        
    
    return sorted(answer)


# 그냥 year*12*28 + month*28 + day 로 편하게 생각하자..