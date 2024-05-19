#블로그 참고https://velog.io/@changhee09/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%B9%B4%EB%8D%B0%EC%9D%B8-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98
import sys
input = sys.stdin.readline
while True:
    n = int(input())
    arr = []
    sum = [0]*n
    dp = [-10000]*n
    
    if n==0:
        break
    for i in range(n):
        arr.append(int(input()))
    local_max,global_max = arr[0], arr[0]
    for i in range(1,n):
        # 이전의 최댓값 + 자기 자신 or 자기 자신중 최댓 값 구하기
        local_max = max(arr[i], local_max+arr[i])
        global_max = max(global_max, local_max)
    print(global_max)     