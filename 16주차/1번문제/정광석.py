'''
기차가 어둠을 헤치고 은하수를

N개의 기차가 어둠해치고 은하수

20개 좌석
한 좌석엔 한명
1~N번 매길 때 어떤 기차에 대해 M개 명령 주어짐

1 i x : i번째 기차에 x번째 좌석에 사람

'''



def solution():

    N, M = map(int, input().split())
    train = [0]*N
    for c in range(M):
        cmd = list(map(int, input().split()))
        
        
        #print(cmd)

        if cmd[0] == 1:
            i = cmd[1]-1
            x = cmd[2]-1
            train[i] |= 1<<x
            
        elif cmd[0] == 2:
            i = cmd[1]-1
            x = cmd[2]-1
            train[i] &= ~(1<<x)
            
        elif cmd[0] == 3:
            i = cmd[1]-1
            train[i]= train[i]<<1
            train[i] &= ~(1<<20)
        elif cmd[0] == 4:
            i = cmd[1]-1
            train[i] = train[i]>>1
            
        #print(train)
    train_set = set(train)
    
    #print(train_set)    

    print(len(train_set))

solution()