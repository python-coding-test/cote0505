def solution(s):
    answer = 0
    arr = []
    for i in range(1, len(s)+1):
        shortenStr = ''
        count = 1
        temp = s[:i]
        for j in range(i, len(s)+i, i):
            if temp == s[j:j+i]:
                count += 1
            else:
                if count != 1:
                    shortenStr = shortenStr + str(count) + temp
                else:
                    shortenStr = shortenStr + temp
                temp = s[j:j+i]
                count = 1
        arr.append(len(shortenStr))
    
    answer = min(arr)
    return answer
