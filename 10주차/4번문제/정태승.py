def solution(enroll, referral, seller, amount):
    
    adj = {enroll[i] : referral[i] for i in range(len(referral))}
    revenues = {e:0 for e in enroll}
    
    def go(money, curr):
        if curr not in adj: # 민호 도달 혹은 분배할 돈 1원 미만.
            return
        
        if (money // 10) == 0 :
            revenues[curr] += money
            return

        send = money // 10
        mine = money - send

        revenues[curr] += mine

        go(send, adj[curr])

    for i in range(len(seller)):
        go(100*amount[i], seller[i])
        
        
    return list(revenues.values())

# 시도1 - money 계산 로직 수정.
# def solution(enroll, referral, seller, amount):
    
#     adj = {enroll[i] : referral[i] for i in range(len(referral))}
#     revenues = {e:0 for e in enroll}
    
#     def go(money, curr):
#             if curr not in adj:
#                 return
            
#             if money*0.1 < 1 :
#                 revenues[curr] += money
#                 return
            
#             revenues[curr] += round(money * 0.9)
#             go(round(money * 0.1), adj[curr])
        
#     for i in range(len(seller)):
#         go(100*amount[i], seller[i])
        
        
#     return list(revenues.values())


# 시도2 - money 계산 로직 수정
# def solution(enroll, referral, seller, amount):
    
#     adj = {enroll[i] : referral[i] for i in range(len(referral))}
#     revenues = {e:0 for e in enroll}
    
#     def go(money, curr):
#         if curr not in adj: # 민호 도달 혹은 분배할 돈 1원 미만.
#             return
        
#         if money <= 10 :
#             revenues[curr] += money
#             return

#         send = money // 10
#         mine = money - send

#         revenues[curr] += mine

#         go(send, adj[curr])

#     for i in range(len(seller)):
#         go(100*amount[i], seller[i])
        
        
#     return list(revenues.values())

