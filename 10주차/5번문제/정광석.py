'''
언어 3 중 1
직군 2 중 1
경력 2 중 1
푸드 2 중 1
'''

info = ["java backend junior pizza 150","python frontend senior chicken 210",
        "python frontend senior chicken 150","cpp backend senior pizza 260",
        "java backend junior chicken 80","python backend senior chicken 50"]

query = ["java and backend and junior and pizza 100",
         "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250",
         "- and backend and senior and - 150",
         "- and - and - and chicken 100","- and - and - and - 150"]	
result = [1,1,1,1,2,4]



def solution(info, query):
    answer = [] # 몇 명인지 저장

    # info 전처리
    info_list = []
    for i in info: 
        info_list.append(i.split())
    #print(info_list)
       
    query_list = []
    for q in query:
        query_list.append(q.replace("and", ' ').split())
        
    #print(query_list)
    def cal(q,j):
        
        if int(q[4]) > int(j[4]):
            return False


        else:
            for i in range(4):
                if q[i]=='-' :
                    continue
                if q[i] != j[i]:
                    return False
                    
                
        return True
        
        
        

    
    for q in query_list:
        count = 0
        for j in info_list:
            if cal(q,j):
                count += 1


        answer.append(count)


    return answer


print(solution(info, query))
