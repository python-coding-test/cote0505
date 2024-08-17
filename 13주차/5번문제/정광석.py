'''
멘토 n명 1~k 분류되는 상담 유형 있음

각 멘토 k개 상담 유형 중 하나만 담당 가능


멘토는 자신이 담당하는 유형의 상담만 가능, 다른 유형은 불가능
멘토는 동시에 참가자 한명과 상담 간으
상담 시간은 정확히 참가자가 요청한 시간만큼


규칙
- 상담 요청 : 상담 유형 담당 멘토 중 상담 중이지 않은 멘토 배정
- 모두 상담중이면 참가자는 대기, 참가자 기다린 시간은 요청때부터 상담 시작때까지 기다린 시간
- 우선 순위 존재


기다린 시간을 최소로 해야함


'''


k,	n,	reqs,	result = \
 2,	3,	[[5, 55, 2], [10, 90, 2], [20, 40, 2], [50, 45, 2], [100, 50, 2]],	90

#3,	5	,[[10, 60, 1], [15, 100, 3], [20, 30, 1], [30, 50, 3], [50, 40, 1], [60, 30, 2], [65, 30, 1], [70, 100, 2]]	,25



def distribute_items(n, k, min_val=1):
    def helper(n, k, min_val):
        if k == 1:
            # 남은 모든 아이템을 마지막 칸에 넣음
            return [[n]]
        
        distributions = []
        for i in range(min_val, n - k + 2):  # 각 칸에 최소 min_val 개 이상 넣음
            for rest in helper(n - i, k - 1, min_val):
                distributions.append([i] + rest)
        return distributions
    
    return helper(n, k, min_val)
#print (distribute_items(4,4))
# 예시: 5개의 아이템을 3칸에 분배 (각 칸에 최소 1개)
# 시각, 상담 시간, 상담 유형

from heapq import heappush , heappop

def solution(k, n, reqs):
    answer = 10000000

    result = distribute_items(n, k)
    #print(result)
    table = [[] for _ in range(k)]

    for a,b,c in reqs:
        table[c-1]



    for res in result:
        time = 0
        working = [[] for _ in range(k)]

        for a,b,c, in reqs:
            c = c-1
            if len(working[c]) < res[c]: # x 타입에 멘토가 남으면
                heappush(working[c], a+b)
            else:
                finsih_soon = heappop(working[c])
                if finsih_soon>= a: #젤 빨리 끝나는 멘토보다 a가 빠르면 기다려야 한다.
                    time += finsih_soon - a
                    heappush(working[c], finsih_soon+b)
                
                else:
                    heappush(working[c], a+b)





        if time < answer:
            answer = time
        







    return answer


print(solution(k, n, reqs))

