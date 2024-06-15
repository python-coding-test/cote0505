def solution(cap, n, deliveries, pickups):
    answer = 0
    avail = [0,0]

    for i in range(n-1,-1,-1):
        while avail[0] < deliveries[i] or avail[1] < pickups[i]:
            avail[0] += cap
            avail[1] += cap
            answer += 2*(i+1)

        avail[0] -= deliveries[i]
        avail[1] -= pickups[i]


    return answer