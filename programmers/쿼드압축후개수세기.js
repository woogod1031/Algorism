// 240610

function solution(arr) {
  if (arr.every((ar) => ar.every((v) => v == 1))) return [0, 1];
  if (arr.every((ar) => ar.every((v) => v == 0))) return [1, 0];

  const len = arr.length / 2;

  const q1 = arr.slice(0, len).map((ar) => ar.slice(0, len));
  const q2 = arr.slice(0, len).map((ar) => ar.slice(len));
  const q3 = arr.slice(len).map((ar) => ar.slice(0, len));
  const q4 = arr.slice(len).map((ar) => ar.slice(len));

  return [q1, q2, q3, q4].reduce(
    (ac, cu) => {
      const [i, j] = solution(cu);
      return [ac[0] + i, ac[1] + j];
    },
    [0, 0]
  );
}

// function compress(array) {
//   if (array.every((arr) => arr.every((ar) => ar == 0))) return [1, 0];
//   if (array.every((arr) => arr.every((ar) => ar == 1))) return [0, 1];

//   const len = array.length / 2;

//   if (len == 1) {
//     return array.reduce(
//       ([az, ao], c) => {
//         c.forEach((n) => {
//           if (n == 0) az++;
//           else if (n == 1) ao++;
//         });
//         return [az, ao];
//       },
//       [0, 0]
//     );
//   }

//   let total = [0, 0];
//   for (let i = 0; i < 4; i++) {
//     const row = i < 2 ? 0 : len;
//     const col = i % 2 == 0 ? 0 : len;
//     const [z, o] = compress(
//       array.slice(row, row + len).map((ar) => ar.slice(col, col + len))
//     );
//     total[0] += z;
//     total[1] += o;
//   }
//   return total;
// }

// function solution(arr) {
//   return compress(arr);
// }

// console.log(
//   solution([
//     [1, 1, 0, 0],
//     [1, 0, 0, 0],
//     [1, 0, 0, 1],
//     [1, 1, 1, 1],
//   ])
// );

console.log(
  solution([
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1, 1],
    [0, 1, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 1, 1, 1],
  ])
);
