answer = []
max_diff = 0

def dfs(n, appech_info, ryan_info, stage):
    global answer, max_diff
    
    if stage == 11:
        if n != 0:
            ryan_info[10] = n
        
        diff = calculate_diff(appech_info, ryan_info)
        
        if diff <= 0:
            return
        result = ryan_info[:]
        if max_diff < diff:
            answer = [result]
            max_diff = diff
        if max_diff == diff:
            answer.append(result)
        return
    
    if n > appech_info[stage]:
        ryan_info.append(appech_info[stage] + 1)
        dfs(n - appech_info[stage] - 1, appech_info, ryan_info, stage + 1)
        ryan_info.pop()
    
    ryan_info.append(0)
    dfs(n, appech_info, ryan_info, stage + 1)
    ryan_info.pop()
                
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
        
    dfs(n, info, [] , 0)
                    
    if (len(answer) == 0):
        answer = [-1]
                    
    answer.sort(key=lambda x: x[::-1], reverse=True)
    
    return answer
