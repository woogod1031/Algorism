function solution(info, query) {
  const joiner = info.map((v) => v.split(" "));

  const answer = query.map((c) => {
    const condition = c.split(" ").filter((v) => v != "and");

    return joiner.filter((j) => {
      return j.every((k, idx) => {
        if (condition[idx] == "-") return true;
        if (idx == 4 && +k >= +condition[idx]) return true;
        if (condition[idx] == k) return true;
        return false;
      });
    }).length;
  });
  return answer;
}

console.log(
  solution(
    [
      "java backend junior pizza 150",
      "python frontend senior chicken 210",
      "python frontend senior chicken 150",
      "cpp backend senior pizza 260",
      "java backend junior chicken 80",
      "python backend senior chicken 50",
    ],
    [
      "java and backend and junior and pizza 100",
      "python and frontend and senior and chicken 200",
      "cpp and - and senior and pizza 250",
      "- and backend and senior and - 150",
      "- and - and - and chicken 100",
      "- and - and - and - 150",
    ]
  )
);
