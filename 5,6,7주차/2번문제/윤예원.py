#풀이 https://school.programmers.co.kr/questions/53863
def solution(cap, n, deliveries, pickups): 
    answer, dcap, pcap = 0,0,0
    
    # 배달과 수거를 역순으로 진행
    for i in range(n-1, -1, -1):
        # 배달할 상자가 남아있을 경우
        if deliveries[i] != 0 or pickups[i] != 0:
            # 물류창고까지 이동한 거리
            cnt = 0
            # 배달할 상자를 최대 cap개까지 실어 이동
            while dcap < deliveries[i] or pcap< pickups[i]:
                cnt+=1
                dcap +=cap
                pcap+=cap
            dcap-=deliveries[i]
            pcap-=pickups[i]
            answer += ((i+1)*cnt*2)
    return answer