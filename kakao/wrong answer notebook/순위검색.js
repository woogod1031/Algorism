function rc(array, index, map, score) {
  const key = array.join("");
  if (Array.isArray(map[key])) map[key].push(score);
  else map[key] = [score];

  for (let i = index; i < array.length; i++) {
    const copy = array.slice();
    copy[i] = "-";
    rc(copy, i + 1, map, score);
  }
}

function bs(arr, score) {
  if (!arr) return 0;
  let left = 0;
  let right = arr.length;

  while (left < right) {
    let mid = Math.floor((left + right) / 2);

    if (arr[mid] >= score) right = mid;
    else left = mid + 1;
  }

  return arr.length - left;
}

function solution(info, query) {
  const map = {};

  info.forEach((v) => {
    const array = v.split(" ");
    const score = array.pop();
    rc(array, 0, map, score);
  });

  for (let key in map) map[key].sort((a, b) => a - b);

  return query.map((string) => {
    let qs = string.split(" ").filter((v) => v != "and");
    const score = Number(qs.pop());
    qs = qs.join("");
    return bs(map[qs], score);
    // if (Array.isArray(map[qs])) {
    //   // map[qs].sort((a, b) => a - b);
    //   return bs(map[qs], score);
    // }
    // return 0;
  });
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
      "java and backend and junior and pizza 100", // java backend junior pizza 100
      "python and frontend and senior and chicken 200",
      "cpp and - and senior and pizza 250",
      "- and backend and senior and - 150", // - backend senior - 150
      "- and - and - and chicken 100",
      "- and - and - and - 150",
    ]
  )
);
