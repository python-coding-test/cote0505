from itertools import combinations

def solution(relation):
    # 후보키의 최대개수. (유일성 + 최소성)
    fields = [i for i in range(len(relation[0]))]
    alter_keys = []
    def check_min(c):
        # 1. 최소성 확인 (특정 키의 부분집합인지 확인.)
        for key in alter_keys:
            if key.issubset(c):
                return False
        return True

    def check_unique(c): 
        # 2. 유일성 확인 (중복 레코드 확인)
        dic = {}
        for r in relation:
            k = ''
            for tmp_c in c:
                k+=str(r[tmp_c])

            if k not in dic:
                dic[k] = True
            else:
                return False
                    
        return True 
    
    for n in range(1, len(relation[0])+1): # 1.. 2.. 3.. 개 뽑기
        for c in list(combinations(fields, n)):
            
            c_set = set(c)
            
            # 최소성 확인. & 유일성 확인.
            if check_min(c_set) and check_unique(c_set):
                alter_keys.append(c_set)    

        
            
            
    return len(alter_keys)