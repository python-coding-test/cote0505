def solution(k, dungeons):

#     dungeons.sort(key = lambda x : (x[0],x[1]))

#     maxNum = 0
#     for i,v in enumerate(dungeons):
#         if v[0] > k:
#             continue
#         hp = k-v[1]
#         num = 1

#         for j,v2 in enumerate(dungeons):
#             if i==j:
#                 continue

#             if hp < v2[0]:
#                 break

#             hp -= v2[1]
#             num += 1
#         maxNum = max(maxNum, num)

    # gpt 참조해서 개선한 코드입니다
    visited = [False] * len(dungeons)

    def dfs(k, cnt):
        max_cnt = cnt

        for i in range(len(dungeons)):
            if not visited[i] and k >= dungeons[i][0]:
                visited[i] = True
                max_cnt = max(max_cnt, dfs(k - dungeons[i][1],  cnt + 1))
                visited[i] = False

        return max_cnt

    return dfs(k, 0)