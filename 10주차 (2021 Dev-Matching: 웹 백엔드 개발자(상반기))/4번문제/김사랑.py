def solution(enroll, referral, seller, amount):
    answer = []
    graph = {}
    income = {i: 0 for i in enroll}  # 이름: 수익

    # 자식: 부모
    for i in range(len(enroll)):
        graph[enroll[i]] = referral[i]

    def distribution(child, amount):
        if child == '-' or amount < 1:  # 1원 이하면 자식이 가져감?
            return
        parent = graph[child]
        pay = int(amount * 0.1)  # amount // 10
        income[child] += (amount - pay)
        distribution(parent, pay)

    for i, child in enumerate(seller):
        initial_amount = amount[i] * 100
        distribution(child, initial_amount)
    
    answer = [income[name] for name in enroll]
    return answer
