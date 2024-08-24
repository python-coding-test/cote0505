'''
인사고과

인센티브 지급

사원마다 근무 태도, 동료 평가 점수가 각각 있는데
어떤 사원이 다른 사원보다 두 점수가 모두 낮은 상황이 하나라도 있으면 그 사원은 인센티브 못받음
그렇지 않은 사원은 두 점수 합 높은순 석차
동일한 점수이면 동점, 다음 석차는 그만큼 밀림

각 사원 근태 동료평가 주어지고 석차 return 하기

인센티브 못받는 사람 걸러내고
받는 사람 중 석차 결정하기
'''

#[[7, 1], [6, 6], [5, 4], [5, 4], [6, 6]] ,3# 
scores,	result =[[2,1],[2,2],[2,3],[3,1]],1#[[3,2],[2,3],[3,2],[2,3]],1#[[7, 1], [6, 6], [5, 4], [5, 4], [6, 6]] ,3# [[2,2],[1,4],[3,2],[3,2],[2,1]],	4
def solution(scores):
    answer = 0
    wanho = scores[0]

    scores.sort(reverse=True, key=lambda x: (x[0], -x[1]))  # 첫 번째 요소로 내림차순, 두 번째 요소로 내림차순 정렬
    filtered_scores = []
    max_b = float('-inf')
    max_a = float('-inf')
    for a, b in scores:
        if b >= max_b and a>=max_a:
            filtered_scores.append([a, b])
            max_b = b

    #print(filtered_scores)
    if wanho not in filtered_scores:
        return -1 # 완호가 지워짐
    
    
    sum_scores =  [sum(i) for i in filtered_scores]
    sum_scores.sort(reverse=True)
    rank = 1
    for s in sum_scores:
        if s == wanho[0]+wanho[1]:
            return rank
        rank+=1
    

    print(rank)

    


    return answer

print(solution(scores))