function solution(info, query) {
  function getCombination(arr, score, map, start) {
    const key = arr.join("");
    if (Array.isArray(map[key])) map[key].push(score);
    else map[key] = [score];

    for (let i = start; i < arr.length; i++) {
      let combiArr = arr.slice();
      combiArr[i] = "-";
      getCombination(combiArr, score, map, i + 1);
    }
  }

  function binarySearch(arr, score) {
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

  const map = {};

  for (let i = 0; i < info.length; i++) {
    const infos = info[i].split(" ");
    const score = infos.pop();
    getCombination(infos, score, map, 0);
  }

  for (let key in map) map[key].sort((a, b) => a - b);

  const result = [];

  for (let i = 0; i < query.length; i++) {
    let queryString = query[i].split(" ").filter((v) => v != "and");
    const score = Number(queryString.pop());
    queryString = queryString.join("");
    let scoreIndex = binarySearch(map[queryString], score);
    result.push(scoreIndex);
  }
  return result;
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
