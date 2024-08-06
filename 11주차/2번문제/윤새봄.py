def solution(play_time, adv_time, logs):
    answer = ''
    
    def time_to_sec(time):
        h, m, s = map(int, time.split(":"))
        return h*3600 + m*60 + s
    
    def sec_to_time(sec):
        h = sec//3600
        m = sec%3600//60
        s = sec%3600%60
        # if (h<10):
        #     h = '0'+str(h)
        # else:
        #     h = str(h)
        h = '0' + str(h) if h<10 else str(h)
        m = '0' + str(m) if m<10 else str(m)
        s = '0' + str(s) if s<10 else str(s)
        return h+":"+m+":"+s 
        
    play_time = time_to_sec(play_time)
    adv_time = time_to_sec(adv_time)
    
    all_time = [0 for i in range(play_time+1)]
    
    for log in logs:
        start, end = map(time_to_sec, log.split("-"))
        all_time[start]+=1 # all_time[i] = i시점에 시청하는 사람 수
        all_time[end]-=1   
    
    # all_time[i] = (i-1)초에서 i초 즉, 1초 동안 시청한 사람의 수
    for i in range(1, len(all_time)):
        all_time[i] = all_time[i] + all_time[i-1]
    
    # all_time[i] = 0초부터 i초까지 누적 시청한 사람의 수
    for i in range(1, len(all_time)):
        all_time[i] = all_time[i] + all_time[i-1]
        
    most_view = all_time[adv_time-1]
    max_time = 0
    
    for i in range(adv_time, play_time):
        if (most_view < all_time[i] - all_time[i-adv_time]):
            most_view = all_time[i] - all_time[i-adv_time]
            max_time = i-adv_time+1
        
    answer = sec_to_time(max_time)    
        
    return answer