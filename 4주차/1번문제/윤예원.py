import collections
def solution(friends, gifts):
    give = collections.defaultdict(int)
    get = collections.defaultdict(int)
    giveget = collections.defaultdict(int)
    present = collections.defaultdict(int)
    nxt = collections.defaultdict(int) #다음달
    for g in gifts:
        name = g.split()
        giveget[(name[0], name[1])]+=1
        give[name[0]] +=1
        get[name[1]] +=1
        present[name[0]] = give[name[0]]-get[name[0]]
        present[name[1]] = give[name[1]]-get[name[1]]
    for i in range(len(friends)):
        for j in range(i+1, len(friends)):
            f1 = friends[i]
            f2 = friends[j]
            #비교
            if giveget[(f1, f2)] == giveget[(f2, f1)]: #선물지수를 비교해야하는 경우
                #선물지수 비교
                if present[f1] > present[f2]:
                    nxt[f1]+=1
                elif present[f1] < present[f2]:
                    nxt[f2]+=1
            elif giveget[(f1, f2)] > giveget[(f2, f1)]:
                nxt[f1]+=1
            elif giveget[(f1, f2)] < giveget[(f2, f1)]:
                nxt[f2]+=1
    print(nxt)
    if nxt: 
        max_value = max(nxt.values())
    else:
        max_value = 0   
    return max_value
