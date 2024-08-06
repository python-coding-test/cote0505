# 1차시도 : 시간초과
# def solution(N, stages):
    
#     total = len(stages)
#     dic = {i : 0 for i in range(1, N+1)}
#     ans = []
#     for s in stages:
#         for i in range(1, s):
#             dic[i] += 1

#     for k, v in dic.items():
#         ans.append(((total-v) / total, -k))
#         total = v # 합격한 사람
    
#     ans.sort(reverse=True)
    
#     return list(map(lambda x : -x[1], ans))



def solution(N, stages):
    
    stages.sort()
    
    total = len(stages)
    prev = stages[0]
    cnt = 1
    dic = {i:0 for i in range(1, N+1)}

    for i in range(1, len(stages)):
        curr = stages[i]
        
        if prev == curr:
            cnt+=1
            prev = curr
        else:
            failure_rate = cnt / total
            total -= cnt
            dic[prev] = failure_rate
            prev = curr
            cnt=1
            
    if cnt >= 1: # 마지막 처리
        failure_rate = cnt / total
        if prev in dic:
            dic[prev] = failure_rate
        

    ans = [(v, -k) for k, v in dic.items()]

    ans.sort(reverse=True)

    
    return list(map(lambda x:-x[1], ans))
