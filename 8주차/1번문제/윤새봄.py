def solution(survey, choices):
    answer = ''
    
    score_dict = {'R' : 0, 'T' : 0, 'C' : 0, 'F' : 0, 'J' : 0, 'M' : 0, 'A' : 0, 'N' : 0}
    
    for i in range(len(survey)):
        score = choices[i]
        if (score < 4):
            score_dict[survey[i][0]] += 4-score # 누적 개념으로 가야함.
        elif (score > 4): 
            score_dict[survey[i][1]] += score-4
            
    arr = list(score_dict.items())
    # print(arr)
    
    for i in range(0, len(arr), 2):
        if (arr[i][1] >= arr[i+1][1]):
            answer+=arr[i][0]
        else:
            answer+=arr[i+1][0]
    return answer