#지피티 이용
def find_k(k):
    if k == 1:
        return '0'
    length = 1
    while 2*length<k:
        length*=2
    #중앙을 기준으로 왼쪽에 있음
    if k<=length:
        return find_k(k)
    else:
        return "1" if find_k(k-length) == "0" else "0"

k = int(input())
print(find_k(k))