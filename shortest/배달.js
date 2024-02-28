function solution(N, road, K) {
  const contry = new Array(N + 1).fill(0).map(() => new Array());
  const result = new Array(N + 1).fill(Number.MAX_SAFE_INTEGER);

  road.forEach((e) => {
    const [a, b, c] = e;
    contry[a].push([b, c]);
    contry[b].push([a, c]);
  });

  const arr = [[1, 0]];
  result[1] = 0;

  while (arr.length) {
    const [num, dist] = arr.shift();
    if (result[num] < dist) {
      continue;
    }

    contry[num].forEach((val) => {
      const [target, dit] = val;
      const cost = result[num] + dit;
      if (cost < result[target]) {
        result[target] = cost;
        arr.push([target, cost]);
      }
    });
  }

  // return result.slice(1).reduce((acc, cur) => {
  //   if (cur <= K) {
  //     return (acc += 1);
  //   }
  //   return acc;
  // }, 0);
  return result.slice(1).filter((v) => v <= K).length;
}

solution(
  5,
  [
    [1, 2, 1],
    [2, 3, 3],
    [5, 2, 2],
    [1, 4, 2],
    [5, 3, 1],
    [5, 4, 2],
  ],
  3
);
