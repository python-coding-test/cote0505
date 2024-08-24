def solution(picks, minerals):
    answer = 0
    sum = 0
    
    #곡괭이 수를 구함.
    for pick in picks:
        sum += pick
    
    if (len(minerals) > sum):
        minerals = minerals[:sum*5]
    #print(minerals)
    
    new_minerals = [[0, 0, 0] for i in range(len(minerals)//5+1)]
    #print(new_minerals)
    
    for i in range(len(minerals)):
        if (minerals[i]=='diamond'):
            new_minerals[i//5][0]+=1
        elif (minerals[i]=='iron'):
            new_minerals[i//5][1]+=1
        elif (minerals[i]=='stone'):
            new_minerals[i//5][2]+=1
    
    # 다이아몬트, 철, 돌이 많은 순서대로 나열하고 다이아몬드, 철, 돌 공갱이가 있는 대로 적용함.
    # 다이아몬드 곡갱이가 제일 효율이 높고 그다음으로 철 곡갱이가 효율이 높음.
    new_minerals.sort(key=lambda x:(x[0],x[1],x[2]), reverse=True)
    
    for i in new_minerals:
        dia, iron, stone = i
        # 다이아몬드, 철, 돌 공갱이가 있는 대로 적용함.
        for j in range(len(picks)):
            if(picks[j]>0 and j==0):
                picks[j]-=1
                answer += dia + iron + stone
                break
            elif (picks[j]>0 and j==1):
                picks[j]-=1
                answer += dia*5 + iron + stone
                break
            elif (picks[j]>0 and j==2):
                picks[j]-=1
                answer += dia*25 + iron*5 + stone
                break
    
    
    return answer