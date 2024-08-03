### 1차 시도 (실패)
# def solution(play_time, adv_time, logs):
    
#     max_acc_time = 0
    
#     h, m, s = map(int, play_time.split(':'))
#     play_times = h*60*60+m*60+s
    
#     h, m, s = map(int, adv_time.split(':'))
#     adv_times = h*60*60+m*60+s
    
#     if play_times == adv_times: # 재생시간이 같을 때.
#         return '00:00:00'
    
#     logss = []
    
#     for l in logs:
#         t1, t2 = l.split('-')
#         h1, m1, s1 = map(int, t1.split(':'))
#         h2, m2, s2 = map(int, t2.split(':'))
#         st_time = (h1*60*60+m1*60+s1)
#         ed_time = (h2*60*60+m2*60+s2)
        
#         logss.append((st_time, ed_time))
        
#     logss.sort()
    
    
#     for t in range(play_times):
#         adv_st_time = t
#         adv_ed_time = t + adv_times
        
#         # 공익 광고 시간을 넘길 때.
#         if adv_ed_time > play_times:
#             break
            
#         # 광고 st 이상 & 광고 ed 보다 작은 유저st를 가진 값들 구하기.
#         groups = []
#         for l in logss:
#             if adv_st_time <= l[0] < adv_ed_time:
#                 groups.append(l)
            
#             if l[0] >= adv_ed_time:
#                 break
        
#         # 해당 그룹들로 누적 시청시간 구하기.
#         if not groups :
#             continue
#         acc_time = 0
#         for g in groups:
#             if g[1] >= adv_ed_time: # 해당 그룹의 ed이 adv_ed 이상일 때
#                 acc_time += (adv_ed_time - g[0])
#             else :
#                 acc_time += (g[1] - g[0])
        
#         if max_acc_time < acc_time:
#             max_acc_time = acc_time
#             answer = '%02d:%02d:%02d'%(t//(60*60), t%(60*60)//60, t%(60*60)%60)
    
#     return answer

# 2차 시도. 누적합. 블로그참고 (https://velog.io/@rltjr1092/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EA%B4%91%EA%B3%A0%EC%82%BD%EC%9E%85-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%92%80%EC%9D%B4)
def sec_to_time(sec):
    h, m, s = sec // 3600, sec % 3600 // 60, sec % 60
    return f'{h:02}:{m:02}:{s:02}'

def time_to_sec(time):
    h, m, s = map(int, time.split(':'))
    return h*60*60+m*60+s

def solution(play_time, adv_time, logs):
    
    play = time_to_sec(play_time)
    adv = time_to_sec(adv_time)
    
    if play == adv:
        return '00:00:00'
    
    viewers = [0 for _ in range(100*60*60+1)] # 시간별 시청자 수. 
    
    for l in logs: # 시간대별 시청자 수 구하기
        st_t, ed_t = map(time_to_sec, l.split('-'))
        viewers[st_t] += 1
        viewers[ed_t] -= 1
        
    
    # 누적합 생성하기
    p = 0
    viewers[1] += (viewers[0] + viewers[0])
    for i in range(2, len(viewers)):
        viewers[i] += 2*viewers[i-1] - viewers[i-2]
        # viewers[i] += (viewers[i-1] + (viewers[i-1]-viewers[i-2])) (i-2, i-3) 구간합 구한 다음 (i-1)의 값 더해주면 (i)의 값을 구할 수 있음.
        
    # t == 0. 길이가 adv로 주어질 때. 구간의 최대합 구하기.
    mx = viewers[adv]
    answer = 0
    
    for t in range(1, play-adv+1): 
        view = viewers[t + adv - 1] - viewers[t-1]
        if view > mx:
            mx = view
            answer = t
    
    
        
    return sec_to_time(answer)