answer = []
max_diff = 0

def dfs(n, appech_info, ryan_info, stage):
    global answer, max_diff
        
    # 모든 스테이지를 다 돌았을 때
    if stage == 11:
        
        if n != 0:
            ryan_info[10] = n  # 남은 화살을 0점에 맞춘 것으로 설정
        
        #print(f"n : {n}")
        #print(f"appech_info : {appech_info}")
        #print(f"ryan_info : {ryan_info}")
        
        diff = calculate_diff(appech_info, ryan_info)
        
        if diff <= 0:
            return
        
        result = ryan_info[:]
        
        if max_diff < diff:
            answer = [result]
            max_diff = diff
        elif max_diff == diff:
            answer.append(result)
        return
    
    # 라이언이 현재 단계에서 더 많은 화살을 쏠 수 있는 경우
    if n > appech_info[stage]:
        ryan_info[stage] += appech_info[stage]+1  # 현재 점수에 대해 라이언이 한 발 더 쏘기
        dfs(n - (appech_info[stage] + 1), appech_info, ryan_info, stage + 1)
        ryan_info[stage] -= appech_info[stage] + 1  # 원래대로 되돌리기  # 원래대로 되돌리기
    
    # 현재 점수에 대해 라이언이 화살을 쏘지 않는 경우
    dfs(n, appech_info, ryan_info, stage + 1)
    ryan_info[stage] = 0
    

def calculate_diff(info, shoot):
    peach_score, ryan_score = 0, 0
    for i in range(11):
        if (info[i], shoot[i]) == (0, 0):
            continue
        if info[i] >= shoot[i]:
            peach_score += (10 - i)
        else:
            ryan_score += (10 - i)
    return ryan_score - peach_score

def solution(n, info):
    global answer, max_diff
    answer = []
    max_diff = 0

    # 라이언의 초기 정보 설정
    ryan_info = [0] * 11
    dfs(n, info, ryan_info, 0)
                
    if len(answer) == 0:
        return [-1]
    
    # 점수 차이가 최대인 경우, 낮은 점수를 더 많이 맞힌 경우로 정렬
    answer.sort(key=lambda x: x[::-1], reverse=True)
    
    return answer[0]
