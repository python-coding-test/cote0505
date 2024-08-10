'''

신규 기존 스테이지 차이가 너무 크다

동적으로 게임 시간을 늘려 난이도 조절

실패율 구하는 부분

전체 스테이지 개수 N

게임 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages


실패율 : 
스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수

'''

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3] #이용자 8명
result = [3,4,2,1,5] # N = 5



from collections import defaultdict

def solution(N, stages):
    answer = defaultdict(int)
    
    # 총 8명 = len(stages)
    # 각 문제 i 실패율 = i 개수 / 시도한 인원 수(i 이상 값을 가진 애들)

    totalman = len(stages)
    failman = 0


    for i in range(1,N+1): # 스테이지 개수 N개에 대해서
        
        if failman>=totalman: 
            answer[i]=0
            continue
        i_stage_fail = stages.count(i)
        answer[i] = i_stage_fail / (totalman-failman)

        #print(i_stage_fail)
        #print(totalman-failman)
        failman+=i_stage_fail


    answer = sorted(answer, key = lambda x : answer[x], reverse=True)
        
    return answer

print(solution(N, stages))