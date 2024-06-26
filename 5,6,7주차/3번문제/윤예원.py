from itertools import product
def solution(users, emoticons):
    n,m = len(users), len(emoticons)
    max_subscribers = 0
    max_sales = 0
    ratio = [0.1, 0.2, 0.3, 0.4]
    discount_comb = [list(combo) for combo in product(ratio, repeat=m)]
    for comb in discount_comb:
        subscribers = 0
        sales = 0            
        for i in range(n):
            rate, price = users[i]
            total_cost = 0
            for j in range(m):
                if comb[j] >= rate/100:
                    total_cost+=emoticons[j]*(1-comb[j])
            if total_cost >= price:
                subscribers+=1
            else:
                sales+=total_cost
        if subscribers > max_subscribers or (subscribers == max_subscribers and sales> max_sales):
            max_subscribers=subscribers
            max_sales= sales
    return [max_subscribers, int(max_sales)]
