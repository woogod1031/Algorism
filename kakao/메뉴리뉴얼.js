function getCombination(arr, num) {
  if (num == 1) return arr.map((a) => [a]);
  const result = [];
  arr.forEach((fixed, i) => {
    const rest = arr.slice(i + 1);
    const combis = getCombination(rest, num - 1);
    result.push(...combis.map((com) => [fixed, ...com]));
  });
  return result;
}

function solution(orders, course) {
  const result = [];
  course.forEach((num) => {
    const orderMap = {};
    orders.forEach((order) => {
      const orderArr = order.split("");
      const allCombis = getCombination(orderArr, num);
      allCombis.forEach((com = []) => {
        const joinArr = com.sort().join("");
        if (orderMap[joinArr]) {
          orderMap[joinArr]++;
        } else {
          orderMap[joinArr] = 1;
        }
      });
    });
    const combis = Object.entries(orderMap).reduce(
      (acc, [key, value]) => {
        if (value == acc[0]) {
          acc[1].push(key);
          return acc;
        }
        if (value > acc[0]) {
          return [value, [key]];
        }
        if (value < acc[0]) {
          return acc;
        }
      },
      [0, []]
    );
    if (combis[0] >= 2) {
      result.push(...combis[1]);
    }
  });
  return result.sort();
}

console.log(
  solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]).sort()
);
// ["AC", "ACDE", "BCFG", "CDE"]
// A B C F G
// A C
// C D E
// A C D E
// 2
// 3
// 4
