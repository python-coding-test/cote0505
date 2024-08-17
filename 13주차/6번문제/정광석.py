'''

대부분이 아이기스 군사기지에  집중

요격

최소로 사용한 미사일 요격


2차원 공간

x축 평행 직선 개구간,
B 특정 x좌표에서 y축에 수평이 되도록 미사일 발사

해당 x좌표에 걸친 모든 미사일 관통, 한번에 요격가능

s,e 개구간이라서 s,e에서 발사하면 요격 불가
요격 미사일은 x 실수 발사 가능

최소 미사일 개수 구하기
개구간



'''
from collections import defaultdict

targets,	result = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]],	3
# def solution(targets):
#     answer = 0

#     targets.sort()
    
    
#     targ_dict = defaultdict(int)
    
#     for s,e in targets:
#         for i in range(s,e,1):
#             targ_dict[i]+=1
    
#     #print(targ_dict)
#     while targets:
#         max_idx = max(targ_dict, key=targ_dict.get)
#         #print(targets)
#         #print(max_idx)
#         for i in targets:
#             s,e = i
#             if s<=max_idx or max_idx<=e:
#                 targets.remove(i)
#                 for j in range(s,e,1):
#                     targ_dict[j]-=1
                

     
        
       
        
#         answer+=1
        
       
#     #print(answer)
    



    


#     return answer


def solution(targets):
    # 구간의 종료 지점을 기준으로 정렬
    targets.sort(key=lambda x: x[1])
    #print(targets)
    answer = 0
    last_missile = - 10000000 # 마지막으로 발사한 미사일의 위치 초기화

    for start, end in targets:
       
        if last_missile <= start:
            answer += 1
            last_missile = end  # 새로운 미사일은 현재 구간의 끝에 발사
    
    return answer

print(solution(targets))
