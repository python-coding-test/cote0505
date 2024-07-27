'''
24/7/16

불량 이용자 신고, 처리 결과 메일 발송 시스템

각 유저 한번에 한 명 신고
신고 횟수 제한 없음, 다른 유저 계속 신고 가능

동일 유저 대한 여러번의 신고는 1회로 처리

k 번 이상 신고된 유저는 정지,
정지된 유저를 신고한 유저에게 메일 발송

2번 신고 당한다고 즉시 정지시키는게 아니라
신고 모두 받은 후 카운트



'''



def solution(id_list, report, k):
    answer = [0] * len(id_list)
    num = [0] * len(id_list)
    
    report = list(set(report))
    for i in report:
        num[id_list.index(i.split()[1])] += 1

    for r in report:
        reporter , reported =id_list.index(r.split()[0]), id_list.index(r.split()[1])
        if num[reported] >= k:
            answer[reporter] +=1
    return answer




