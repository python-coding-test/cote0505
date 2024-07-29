def solution(enroll, referral, seller, amount):
    answer = []
    answer = [0 for _ in range(len(enroll))]
    
    dict = {}
    for idx, name in enumerate(enroll):
        dict[name] = idx
    # print(dict) 
    # {'john': 0, 'mary': 1, 'edward': 2, 'sam': 3, 'emily': 4, 'jaimie': 5, 'tod': 6, 'young': 7}
    
    for pair in zip(seller, amount):
        name, money = pair[0], pair[1]*100
        #print(f"sname, smoney : {name}, {money}")
        while(name!="-" and money>0):
            #print(f"name, money : {name}, {money}")
            idx = dict[name]
            answer[idx]+= money - money//10
            money = money//10
            name = referral[idx]
        #print(f"answer : {answer}")
              
    return answer