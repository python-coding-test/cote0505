def solution(friends, gifts):
    people = dict()
    count = dict()
    num = len(friends)
    
    for i in range(num):
        people[friends[i]] = i
        count[i] = 0
    # dict 키에 사람 이름이고 값을 index 값
    # count는 받아야하는 선물 수
    
    arr = []
    for i in range(num):
        arr.append([0] * num)
    # arr : 선물 주고 받은 경우
    for rel in gifts:
        a, b = rel.split()
        peo_a, peo_b = people[a], people[b]
        arr[peo_a][peo_b] += 1
    
    def cal(a, b):
        a_give = sum(arr[a])
        b_give = sum(arr[b])
        a_get, b_get = 0, 0
        for i in range(len(arr)):
            a_get += arr[i][a]
            b_get += arr[i][b]

        a_index = a_give - a_get
        b_index = b_give - b_get
        if a_index > b_index:
            return a
        elif a_index < b_index:
            return b
        else:
            return -1 # 같은 경우
    
    # arr 에 모든 관계 출력
    for i in range(num):
        for j in range(i, num):
            if i == j:
                continue
            if arr[i][j] > arr[j][i]:
                count[i] += 1
            elif arr[i][j] < arr[j][i]:
                count[j] += 1
            else:
                result = cal(i, j)
                if result != -1:
                    count[result] += 1
                else:
                    continue
    
    result = sorted(count.items(), key=lambda x: x[1], reverse=True)
    winner, val = result[0]
    # ? 딕셔너리의 값 중 최대 값을 가지는 키
    # dict의 Val 값 중 최댓값과 키값을 추려
    for i in range(num):
        if i == winner:
            continue
        if count[i] != val: # 다 같은 게 아니면
            return val
    
    return 0


a =  ["muzi", "ryan", "frodo", "neo"]
b =  ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]

print(solution(a, b))