function solution(numbers, hand) {
  function getCoordi(num) {
    const graph = [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9],
      ["*", 0, "#"],
    ];
    let x;
    let y;

    x = graph.findIndex((value) =>
      value.some((v, i) => {
        if (v == num) {
          y = i;
          return true;
        }
        return false;
      })
    );

    return [x, y];
  }

  const result = [];
  let leftNum = "*";
  let rightNum = "#";

  numbers.forEach((number) => {
    if (number == 1 || number == 4 || number == 7) {
      result.push("L");
      leftNum = number;
    }
    if (number == 3 || number == 6 || number == 9) {
      result.push("R");
      rightNum = number;
    }
    if (number == 2 || number == 5 || number == 8 || number == 0) {
      const [leftX, leftY] = getCoordi(leftNum);
      const [rightX, rightY] = getCoordi(rightNum);
      const [numberX, numberY] = getCoordi(number);
      const leftValue = Math.abs(numberX - leftX) + Math.abs(numberY - leftY);
      const rightValue =
        Math.abs(numberX - rightX) + Math.abs(numberY - rightY);
      if (leftValue == rightValue) {
        if (hand == "right") {
          result.push("R");
          rightNum = number;
        }
        if (hand == "left") {
          result.push("L");
          leftNum = number;
        }
      }
      if (leftValue > rightValue) {
        result.push("R");
        rightNum = number;
      }
      if (leftValue < rightValue) {
        result.push("L");
        leftNum = number;
      }
    }
  });
  return result.join("");
}

console.log(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"));
