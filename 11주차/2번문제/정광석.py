'''

공익광고
어떤 구간을 재생했는가
재생 구간 기록 
동시에 재생되는 pip 형태

시청자의 누적 시청 시간이 가장 긴 타임에 광고 삽입


'''


play_time ="02:03:55"
adv_time = "00:14:15"
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]

def solution(play_time, adv_time, logs):
    answer = ''
    def conv(string_time):
        hh,mm,ss = map(int, string_time.split(':'))
        return hh*3600 + mm * 60 + ss
    
    def conv2(sec_time):
        hh, mm, ss = sec_time // 3600, (sec_time%3600)//60, sec_time % 60
        return f'{hh:02}:{mm:02}:{ss:02}' 
    

    time_table = [0] * (conv(play_time)+1)
   
    

    cnt = 0
    logs.sort()
    for l in logs:
        ls, le = l.split('-')
        cls, cle = conv(ls), conv(le)
        time_table[cls] += 1
        time_table[cle] -= 1

    for i in range(1, conv(play_time)):
        time_table[i] = time_table[i-1] + time_table[i]
    for i in range(1, conv(play_time)):
        time_table[i] = time_table[i-1] + time_table[i]
    
    
    
    # for l in logs:
    #     ls, le = l.split('-')
    #     cls = conv(ls)
    #     sum = 0
    #     #print(max)
    #     for i in range(cls, min(conv(adv_time)+cls, conv(play_time))):
    #         sum += time_table[i]
        
    #     if max < sum:
    #         max = sum
    #         answer = ls
        
    #     print(sum)
    max = 0 
    for i in range(conv(play_time)-conv(adv_time)+1):
        sum = 0
        total = time_table[i+conv(adv_time)-1] - time_table[i-1]
        
        if  total > max:
            max = total
            answer = i
    
    return conv2(answer)


print(solution(play_time, adv_time, logs))
