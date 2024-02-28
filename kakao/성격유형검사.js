function solution(survey, choices) {
  const test = [
    ["R", "T"],
    ["C", "F"],
    ["J", "M"],
    ["A", "N"],
  ];
  const scrore = {
    0: 3,
    1: 2,
    2: 1,
    3: 0,
    4: 1,
    5: 2,
    6: 3,
  };
  const resultGraph = {
    R: 0,
    C: 0,
    J: 0,
    A: 0,
    T: 0,
    F: 0,
    M: 0,
    N: 0,
  };

  for (let i = 0; i < survey.length; i++) {
    const [disagree, agree] = survey[i].split("");
    const targetScore = scrore[choices[i] - 1];
    if (choices[i] < 4) {
      resultGraph[disagree] += targetScore;
    }
    if (choices[i] > 4) {
      resultGraph[agree] += targetScore;
    }
  }
  const result = [];
  for (let i = 0; i < 4; i++) {
    const [a, b] = test[i];
    if (resultGraph[a] < resultGraph[b]) {
      result.push(b);
    } else {
      result.push(a);
    }
  }

  return result.join("");
}

console.log(solution(["TR", "RT", "TR"], [7, 1, 3]));
