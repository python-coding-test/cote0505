'''
성궤 행방
봉인된 성궤 잠금장치 - 퍼즐
시계들이 행렬이루는 구조물, 하나의 시계에 시곗바늘 하나만
시계방향, 90도 씩

동서남북 중 하나 가리키고 있음


행렬 꼭짓점 : 인접한 2시계 돌아감
행렬 모서리에 위치한 시계 바늘 돌리면 인접한 3 시계 바늘 같이 돌아감
행렬 안쪽 : 인접한 4개

모든 바늘이 12시 방향 가리키면 퍼즐 해결, 잠금 열림

최소한의 조작

0 : 12시, 1: 3시, 2 : 6시, 3: 9시



'''

clockHands,	result = [[0,3,3,0],[3,2,2,3],[0,3,2,0],[0,3,3,3]],	3

from collections import deque

def solution(clockHands):
    answer = 0
    exp_clock = [ [7 for _ in range(len(clockHands[0])+2)] for _ in range(len(clockHands)+2)]
    
    for i in range(1,len(exp_clock[0])-1):
        for j in range(1,len(exp_clock)-1):
            exp_clock[i][j] = clockHands[i-1][j-1]

    def print_array(arr):
        print()
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                print(arr[i][j] ,end=' ')
            print()

    print_array(exp_clock)
    

    def rot(y,x):
        dy = [0,-1,1,0,0]
        dx = [0,0,0,-1,1]

        for i in range(5):
            ty= y + dy[i]
            tx= x + dx[i]
            if exp_clock[ty][tx] == 7:
                continue
            else:
                exp_clock[ty][tx] = (exp_clock[ty][tx]+1)%4
    
    def solved(arr):
        for i in arr:
            for j in i:
                if j==7:
                    continue
                if j != 0:
                    return False
        return True


    
    
    while True:
        cnt = 0
        if solved(exp_clock):
            answer = cnt
            break


        
        


   


    


    

    return answer

print(solution(clockHands))