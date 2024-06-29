def solution(survey, choices):
    scores = {
        "R":0, "T":0,
        "C":0, "F":0,
        "J":0, "M":0,
        "A":0, "N":0
    }
    for i in range(len(survey)):
        non_agree_type, agree_type = survey[i]
        choice = int(choices[i])
        if choice<=4:
            scores[non_agree_type]+=4-choice
        elif choice > 4:
            scores[agree_type] += choice-4
    result =""
    for i, j in zip("RCJA", "TFMN"):
        if scores[i]>=scores[j]:
            result+=i
        else:
            result+=j
    print(result)
    return result
solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5])