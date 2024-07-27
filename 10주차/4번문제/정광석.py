enroll =["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]	

referral =	["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]

seller	=	["young", "john", "tod", "emily", "mary"]	

amount	=[12, 4, 2, 5, 10]	



def solution(enroll, referral, seller, amount):
    
    tree = dict(zip(enroll, referral))
    answer = dict(zip(enroll, list(0 for _ in range(len(enroll)))))
    sell = dict(zip(seller, amount))


    for s,a in sell.items():
        
        money = a*100
        
        while True:

            if money < 10:
                answer[s] += money
                break
            else:
                answer[s] += money - money//10
                if tree[s] == "-":
                    break
            money = money//10
            s= tree[s]

    

    answer = list(answer.values())
    return answer   

print(solution(enroll, referral, seller, amount))
