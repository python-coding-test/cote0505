from collections import defaultdict

def solution(id_list, report, k):
    answer = []

    complained = defaultdict(list)
    for info in set(report):
        user, target = info.split(' ')
        complained[target].append(user)

    cnt = {}
    for _id in id_list:
        cnt[_id] = 0

    for users in complained.values():
        if len(users) >= k:
            for user in users:
                cnt[user] += 1

    for i in cnt.values():
        answer.append(i)

    return answer