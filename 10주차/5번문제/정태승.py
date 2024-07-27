# 첫번째 시도 - 효율성 통과 X
# def solution(info, query):
#     answer = []
    
#     infos = [list(i.split()) for i in info]
    
#     for q in query:
#         qu = q.replace('and', '').split()
#         n = 0
#         for i in infos:
#             if (qu[0]=='-' or qu[0] == i[0]) and (qu[1]=='-' or qu[1] == i[1]) and (qu[2]=='-' or qu[2] == i[2]) and (qu[3]=='-' or qu[3] == i[3]) and (int(qu[4]) <= int(i[4])):
#                 n+=1
                
#         answer.append(n)
        
        
#     return answer

# 두번째시도 - 모든 경우를 dic으로 만들고 찾기 (그러나 특정 수를 찾을때 이진 탐색을 써야함.)
from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    answer = []
    
    
    
    lang = ['java', 'python', 'cpp', '-']
    position = ['backend', 'frontend', '-']
    career = ['junior', 'senior', '-']
    food = ['pizza', 'chicken', '-']
    
    dic = {}
    for l in lang:
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    dic[(l, position[i], career[j], food[k])] = []
    

    for i in info:
        l, p, c, f, score = i.split()
        
        score = int(score)
        
        dic[(l, p, c, f)].append(score)
        
        # 4C1
        dic[('-', p, c, f)].append(score)
        dic[(l, '-', c, f)].append(score)
        dic[(l, p, '-', f)].append(score)
        dic[(l, p, c, '-')].append(score)
        
        # 4C2
        for o in list(combinations([0,1,2,3], 2)):
            t = [l, p, c, f]
            t[o[0]] = '-'
            t[o[1]] = '-'
            dic[(t[0], t[1], t[2], t[3])].append(score)
            
        # 4C3
        dic[('-', '-', '-', f)].append(score)
        dic[(l, '-', '-', '-')].append(score)
        dic[('-', p, '-', '-')].append(score)
        dic[('-', '-', c, '-')].append(score)
        
        # 4C4
        dic[('-', '-', '-', '-')].append(score)
    
    for d in dic.values():
        d.sort()
    
    for q in query:
        qu = q.replace('and', '').split()
        n = 0
        if (qu[0], qu[1], qu[2], qu[3]) in dic:
            target_list = dic[(qu[0], qu[1], qu[2], qu[3])] # 이 부분 생각해야함.
            idx = bisect_left(target_list, int(qu[4]))
            n += (len(target_list) - idx)
            
                
        answer.append(n)
        
        
    return answer

# 다른 풀이 https://velog.io/@dogcu/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%88%9C%EC%9C%84-%EA%B2%80%EC%83%89
# from itertools import combinations
# from collections import defaultdict
# from bisect import bisect_left

# def solution(information, queries):
#     answer = []
#     dic = defaultdict(list)
#     for info in information:
#         info = info.split()
#         condition = info[:-1]  
#         score = int(info[-1])
#         for i in range(5):
#             case = list(combinations([0,1,2,3], i))
#             for c in case:
#                 tmp = condition.copy()
#                 for idx in c:
#                     tmp[idx] = "-"
#                 key = ''.join(tmp)
#                 dic[key].append(score) 

#     for value in dic.values():
#         value.sort()   

#     for query in queries:
#         query = query.replace("and ", "")
#         query = query.split()
#         target_key = ''.join(query[:-1])
#         target_score = int(query[-1])
#         count = 0
#         if target_key in dic:
#             target_list = dic[target_key]
#             idx = bisect_left(target_list, target_score)
#             count = len(target_list) - idx
#         answer.append(count)      
#     return answer