def solution(lottos, win_nums):
    answer = [7,7]

    for i in lottos:
        if not i:
            answer[0]-=1
            continue

        if i in win_nums:
            answer[0]-=1
            answer[1]-=1

    answer[0] = min(answer[0],6)
    answer[1] = min(answer[1],6)

    return answer