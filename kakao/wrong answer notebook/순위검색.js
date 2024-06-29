const constants = [
  ["cpp", "java", "python"],
  ["backend", "frontend"],
  ["junior", "senior"],
  ["chicken", "pizza"],
];

function rc(array, origin, index) {
  if (index == origin.length) return [array];
  const result = [];
  for (let i = 0; i < origin[index].length; i++) {
    result.push(...rc([...array, origin[index][i]], origin, index + 1));
  }
  return result;
}

function solution(info, query) {
  const result = rc(
    [],
    constants.map((a) => [...a, "-"]),
    0
  );
  const map = new Map();
  result.forEach((v) => {
    map.set(v.join(" and "), []);
  });

  info.forEach((v) => {
    const array = v.split(" ");
    const score = array.pop();
    const _result = rc(
      [],
      array.map((a) => [a, "-"]),
      0
    ).map((_v) => _v.join(" and "));
    _result.forEach((str) => {
      const val = map.get(str);
      map.set(str, [...val, +score]);
    });
  });

  return query.map((string) => {
    const array = string.split(" ");
    const score = array.pop();
    return map.get(array.join(" ")).filter((value) => value >= +score).length;
  });
}

// ("- and - and - and - X");

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
      "java and backend and junior and pizza 100", // java backend junior pizza 100
      "python and frontend and senior and chicken 200",
      "cpp and - and senior and pizza 250",
      "- and backend and senior and - 150", // - backend senior - 150
      "- and - and - and chicken 100",
      "- and - and - and - 150",
    ]
  )
);
