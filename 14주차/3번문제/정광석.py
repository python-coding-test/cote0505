'''
마인 곡괭이 
다이아 철 돌 0~5개 가짐
곡괭이로 광물 캘때 피로도 소모

철 곡으로 다이아 캐면 피로 5 소모되는 식

각 곡괭이는 종류 상관 없이 광물 5개 캐면 더 사용 불가

최소한의 피로도로 광물 캐려고 함


사용할 수 있는 곡괭이중 아무거나 선택 가능
한번 사용했으면 사용못할 때 까지 사용
주어진 순서 대로만
광산에 모든 광물을 캐거나 더 사용할 곡괭이가 없을 때만

다 1 1 1 
철 5 1 1
돌 25 1 

미네랄 50개가 최대 

idea1
곡괭이는 len(result)/5 개 사용
combination으로 선택해서 최적화?

'''
# 하드코딩 : 88.6점 시간초과 24 25 33 35

from itertools import permutations

def solution(picks, minerals):
    effort = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]

    pick_need = min((len(minerals)+4) // 5, sum(picks))
    
   
    my_picks = [0]*picks[0] + [1]*picks[1] + [2]*picks[2]
    
    min_effort = 10000000

  
    for cmb in set(permutations(my_picks, pick_need)):
        total_effort = 0
        mineral_index = 0
        
        for pick in cmb:
            for _ in range(5):
                if mineral_index >= len(minerals):
                    break
                
                mineral = minerals[mineral_index]
                if mineral == "diamond":
                    total_effort += effort[pick][0]
                elif mineral == "iron":
                    total_effort += effort[pick][1]
                else:
                    total_effort += effort[pick][2]
                
                mineral_index += 1
            
           
            if total_effort >= min_effort:
                break
        
        
        min_effort = min(min_effort, total_effort)
    
    return min_effort


# picks = [1, 3, 2]
# minerals = ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]
picks,	minerals,	result = [0, 0, 1], ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"], 125
print(solution(picks, minerals))
