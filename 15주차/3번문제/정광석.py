'''
카드 100장 1~100까지 하나씩
2이상 100이하 자연수 정해서 그 수보다 작거나 같은 숫자 카드 준비
준비한 카드 수 만큼 작은 상자 준비

준비된 상자를 한 장씩 넣고, 상자를 무작위로 섞어 일렬로 나열
나열 후 1번 부터 번호 붙임

상자 하나 선택해서 상자 속 숫자 카드 확인
확인한 카드에 적힌 번호의 상자 열어. 이미 열려있을 때 까지 반복

연 상자 : 1번 그룹
연 상자 는 따로 두기 - 1번만 있으면 게임이 종료



'''
cards,	result = [8,6,3,7,2,5,1,4],	12
def solution(cards):
    answer = 0
    parent = [i for i in range(len(cards))]
    cards = [card - 1 for card in cards]
    def find_parent(a):
        if a==parent[a]: return a
        return find_parent(parent[a])
    
    def union(a,b):
        a = find_parent(a)
        b = find_parent(b)
        
        if a<b:
            parent[a] = b
        else:
            parent[b] = a


    for i in range(len(cards)):
        start = i
        end = cards[i]

        while find_parent(start) != find_parent(end):
            union(start, end)
            start = end
            end = cards[end]

    
    #print(parent)
    count = [0] * len(cards)
    
    for i in range(len(parent)):
        key = find_parent(parent[i])
        count[key] += 1

    count.sort(reverse=True)
    
    answer = count[0]*count[1] if len(count)>1 else 0

    print(parent)


   
        
        




    return answer


print(solution(cards))