'''
피로도 시스템 0 이상 정수

피도로 사용해서 던전 탐험 가능,
최소 필요 피로도 
소모 피로도

최소 필요 피로도 80
소모 피로도 20 이면

유저 남은 80 이상, 던전 탐험 후 60됨

가능한 최대 던전 개수


'''

k,	dungeons,	result  =80,	[[80,20],[50,40],[30,10]],	3



def solution(k, dungeons):
    answer = -1
    visited = [0] * len(dungeons)
    def rec(c, k, visited):
        nonlocal answer

        for i in range(len(dungeons)):
            if not visited[i] and k >= dungeons[i][0]:
                visited[i] = 1
                count = rec(c + 1, k - dungeons[i][1], visited)
                visited[i] = 0
                if answer < count:
                    answer = count
        return c

    
    rec(0, k, visited)

    return answer


print(solution(k, dungeons))