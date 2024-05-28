function solution(n, left, right) {
  // const array = new Array(n).fill(0).map((_, xi) =>
  //   new Array(n).fill(0).map((_, yi) => {
  //     return Math.max(xi + 1, yi + 1);
  //   })
  // );
  const result = [];
  // const [left_x, left_y] = [Math.floor(left / n), left % n];
  // const [right_x, right_y] = [Math.floor(right / n), right % n];
  for (let i = left; i <= right; i++) {
    const [x, y] = [Math.floor(i / n), i % n];

    result.push(Math.max(x + 1, y + 1));
  }
  // const result = [
  //   ...array[left_x].slice(left_y),
  //   ...array.slice(left_x + 1, right_x).reduce((a, c) => [...a, ...c], []),
  //   ...array[right_x].slice(0, right_y + 1),
  // ];
  return result;
}

console.log(solution(4, 7, 14));
