function combinations(arr, level) {
  if (level === 1) return arr.map((v) => [v]);
  const result = [];
  arr.forEach((item, i, origin) => {
    const rest = origin.slice(i + 1);
    const combis = combinations(rest, level - 1);
    const combination = combis.map((v) => [item, ...v]);
    result.push(...combination);
  });
  return result;
}

function solution(relation) {
  const cols = new Array(relation[0].length).fill(0).map((v, i) => i);
  let count = 0;
  let combiLevel = 1;
  const allcases = [];

  while (combiLevel <= cols.length) {
    allcases.push(...combinations(cols, combiLevel++));
  }

  const skip = [];
  let cursor = 0;

  while (cursor < allcases.length) {
    const col = allcases[cursor];
    if (
      skip.filter((item) => item.every((v) => col.includes(v))).length !== 0
    ) {
      cursor++;
      continue;
    }
    const key = relation.flatMap((val) =>
      col.map((item) => val[item]).join("")
    );

    if ([...new Set(key)].length == relation.length) {
      skip.push(col);
      count++;
    }
    cursor++;
  }

  return count;
}

solution([
  ["100", "ryan", "music", "2"],
  ["200", "apeach", "math", "2"],
  ["300", "tube", "computer", "3"],
  ["400", "con", "computer", "4"],
  ["500", "muzi", "music", "3"],
  ["600", "apeach", "music", "2"],
]);
