def solution(id_list, report, k):
    answer = []
    user_count = len(id_list)
    
    set_report = list(set(report))
    
    # print(set_report) # ["ryan con", "ryan con", "ryan con", "ryan con"] --> ["ryan con"] 
    
    user_dict = {}
    report_dict = {}
    for i in range(0, user_count):
        user_dict[id_list[i]] = []
        report_dict[id_list[i]] = 0
    
    # print(user_dict)
    # print(report_dict) # {'muzi': 0, 'frodo': 0, 'apeach': 0, 'neo': 0}
    
    for j in range(0, len(set_report)):
        user, person = map(str, set_report[j].split())
        #print(report_list) # ['muzi', 'frodo']
        user_dict[user].append(person)
        report_dict[person]+=1
        
    #print(user_dict) # {'muzi': ['frodo', 'neo'], 'frodo': ['neo'], 'apeach': ['frodo', 'muzi'], 'neo': []}
    #print(report_dict) # {'muzi': 1, 'frodo': 2, 'apeach': 0, 'neo': 2}
    
    for index, key in enumerate(user_dict):
        answer.append(0)
        if (len(user_dict[key])==0):
            continue
        for item_value in user_dict[key]:
            if (report_dict[item_value]>=k):
                answer[index]+=1
    
    return answer