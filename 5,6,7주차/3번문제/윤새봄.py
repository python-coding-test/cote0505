def solution(users, emoticons):
    answer = [0, 0]
    
    discount = [10, 20, 30, 40]
    discount_set = []
    
    # 할인율에 대한 중복조합 구하기.
    def makeSet(arr, depth):
        if (depth==len(arr)):
            discount_set.append(arr[:])
            return
        for d in discount:
            arr[depth]+=d
            makeSet(arr, depth+1)
            arr[depth]-=d
            
    makeSet([0]*len(emoticons), 0)
    # print(f"discount_set : {discount_set}")
    # discount_set : [[10, 10], [10, 20], [10, 30], [10, 40], [20, 10], [20, 20], [20, 30], 
    # [20, 40], [30, 10], [30, 20], [30, 30], [30, 40], [40, 10], [40, 20], [40, 30], [40, 40]]
    
    for d in discount_set: # 각각의 모든 할인율 중복조합에 대해
        total_profit = 0
        join_plus = 0
        
        for user in users:  # 각각의 user가
            user_discount = user[0]
            user_money = user[1]
            total = 0
            for i in range(len(emoticons)): # emoticon을 비율% 이상의 할인이 있는 구매하는 경우
                if (d[i]>=user_discount):
                    total += emoticons[i]*((100-d[i])/100) # /을 통해 부동소수점 반환 : (100-60)/100 = 0.4
            if (total>=user_money): # 가격 이상의 돈을 이모티콘 구매에 사용한다면, 이모티콘 구매를 취소하고 플러스에 가입.
                join_plus+=1
            else:
                total_profit += total  
        if (answer[0]<join_plus):
            answer=[join_plus, total_profit]
        elif (answer[0]==join_plus):
            if (answer[1]<total_profit):
                answer[1]=total_profit
            
    
    return answer