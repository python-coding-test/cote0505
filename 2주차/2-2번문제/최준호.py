import math

A,B = map(int, input().split())

# # 소수 찾기
# decimal = [0]*(int(math.sqrt(B))+1)
# decimal[2] = 2

# for i in range(3, len(decimal), 2):
#     decimal[i] = i

# for i in range(3, int(math.sqrt(B))+1, 2):
#     if not decimal[i]:
#         continue
#     for j in range(i+i, int(math.sqrt(B))+1, i):
#         decimal[j] = 0

# # def check(n):
# #     if n == 1:
# #         return False
# #     for i in range(2, int(math.sqrt(n))+1):
# #         if n % i == 0:
# #             return False
# #     return True

# # 거의 소수 찾기
# '''
# 어떤 수 (x)의 거듭제곱이 (B) 이하가 되려면, (x^2 <= B)
# (x)는 최소한 (B)의 제곱근 이하의 값이어야 함 (x <= sqrt(B))
# '''
# cnt = 0
# for i in range(2, int(math.sqrt(B))+1):
#     if decimal[i]:
#         temp = i
#         while i <= B / temp:
#             if i >= A / temp:
#                 cnt += 1
#             temp *= i
# print(cnt)

# 에라토스테네스의 체를 사용하여 B의 제곱근까지의 모든 소수를 찾기
def sieve_of_eratosthenes(n):
    prime = [True for _ in range(n+1)] # 모든 수를 소수라고 가정
    p = 2
    while (p * p <= n):
        if prime[p]:
            # 소수의 배수를 모두 제거
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    return [p for p in range(2, n+1) if prime[p]]

# B의 제곱근까지의 소수 리스트를 생성
primes = sieve_of_eratosthenes(int(math.sqrt(B)))

# 거의 소수 찾기
cnt = 0
for prime in primes:
    square = 2
    temp = prime ** square
    while temp <= B:
        if temp >= A:
            cnt += 1
        square += 1
        temp = prime ** square

print(cnt)