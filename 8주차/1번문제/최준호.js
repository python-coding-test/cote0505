function solution(survey, choices) {
  const personalityType = {
    R: 0,
    T: 0,
    C: 0,
    F: 0,
    J: 0,
    M: 0,
    A: 0,
    N: 0,
  };

  let userType;
  for (let i = 0; i < survey.length; i++) {
    if (choices[i] == 4) continue;
    else if (choices[i] < 4) {
      userType = survey[i][0];
    } else {
      userType = survey[i][1];
    }
    personalityType[userType] += Math.abs(4 - choices[i]);
  }

  let check = 0;
  let prevTypeCnt;
  let decideType = ["", "", "", ""];
  for (let [k, v] of Object.entries(personalityType)) {
    if (check % 2) {
      if (v > prevTypeCnt) decideType[Math.floor(check / 2)] = k;
    } else {
      prevTypeCnt = v;
      decideType[Math.floor(check / 2)] = k;
    }
    check++;
  }
  return decideType.join("");
}
