// x보다 크고 x와 비트가 1~2개 다른 수들 중에서 제일 작은 수

function solution(numbers) {
  return numbers.map((n, i) => {
    const binary = n.toString(2).split("");
    // 뒤에서 가장 먼저 나오는 "0"
    const lastZeroIndex = binary.lastIndexOf("0");

    if (lastZeroIndex === -1) {
      // 111 => 1011
      binary.splice(1, 0, "0");
    } else if (binary.length - 1 === lastZeroIndex) {
      // 100 => 101
      binary[lastZeroIndex] = "1";
    } else {
      // 101 => 110
      [binary[lastZeroIndex], binary[lastZeroIndex + 1]] = [
        binary[lastZeroIndex + 1],
        binary[lastZeroIndex],
      ];
    }
    return parseInt(binary.join(""), 2);
  });
}

console.log(solution([2, 7]));
