def solution(id_list, report, k):
    answer = []
    report = list(set(report))  # 중복 신고 제거
    dic_report = defaultdict(set)  # 신고자 - 신고 받은 사람 (report와 같은 set형으로 맞춰줌)
    dic_count = {}  # 신고 받은 사람 - 신고 받은 횟수 / defaultdict(set)

    for i in id_list:
        dic_count[i] = 0

    for i in report:
        sender, receiver = i.split()
        dic_report[sender].add(receiver)
        dic_count[receiver] += 1

    for i in id_list:
        temp = 0
        for j in dic_report[i]:
            if dic_count[j] >= k:
                temp += 1
        answer.append(temp)

    return answer
