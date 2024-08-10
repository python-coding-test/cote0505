# '''

# 모든 인적사항을 디비에 넣기

# 후보키에 대한 고민\

# 관계 데이터베이스 릴레이션의 튜플을 유일하게 식별할수 있는 속성 또는 속성의 집합

# 유일성
# 최소성

# 학번은 후보키 가능

# relation은 2차원 문자열 배열

# 어떻게 후보키를 식별할 수 있나

# '''


relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]

# def combination(arr, r):
#     string = ''
#     def generate(chosen):
#         if len(chosen) == r:
#             print(chosen)
#             return

#     	# 3.
#         start = arr.index(chosen[-1]) + 1 if chosen else 0
#         for nxt in range(start, len(arr)):
#             chosen.append(arr[nxt])
            
#             generate(chosen)
#             chosen.pop()
#     generate([])
#     return 
    



# def solution(relation):
#     answer = 0

#     #전처리 - transpose
#     t_relation = [list(x) for x in zip(*relation)]
#     cnt=  0
#     new_rel = []
#     comb_cnt=1
#     def make(t_relation):
#         nonlocal cnt
#         nonlocal new_rel
        
        
#         if not t_relation:
#             return

#         for x in t_relation:
#             list_len = len(x)
#             if list_len == len(set(x)):
#                 cnt+=1
                
#             else:
#                 new_rel.append(x)

               
             


#         return cnt
        
#     make(t_relation)
#     print(combination(new_rel,1))
#     # print(make(t_relation))
#     # print(new_rel)
#     return answer


# solution(relation)

# def possi(vec, now):
#     for v in vec:
#         if (v & now) == v:
#             return False
#     return True

# def solution(relation):
#     rowSize = len(relation)
#     colSize = len(relation[0])
#     ans = []

#     for i in range(1, 1 << colSize):
#         s = set()

#         for j in range(rowSize):
#             now = ""
#             for k in range(colSize):
#                 if i & (1 << k):
#                     now += relation[j][k]
#             s.add(now)

#         if len(s) == rowSize and possi(ans, i):
#             ans.append(i)

#     return len(ans)

# print(solution(relation))


from itertools import combinations



def solution(relation):
    rowSize = len(relation)
    colSize = len(relation[0])
    ans = []
    def possi(ans, now):
        for v in ans:
            # 현재 조합이 기존 조합의 부분 집합인지 확인
            if set(v).issubset(now):
                return False
        return True

    # 모든 가능한 컬럼 조합 생성
    for r in range(1, colSize + 1):
        for comb in combinations(range(colSize), r):
            s = set()

            for j in range(rowSize):
                now = tuple(relation[j][k] for k in comb)
                s.add(now)

            if len(s) == rowSize and possi(ans, comb):
                ans.append(comb)

    return len(ans)



print(solution(relation))  