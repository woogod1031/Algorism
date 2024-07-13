function solution(numbers) {
  // 콜백 인자로 a, b가 넘어올 때

  // 음수면  [a, b]
  // 양수면  [b, a]

  const answer = numbers.sort((a, b) => {
    return Number(`${b}${a}`) - Number(`${a}${b}`);
  });

  return answer[0] == 0 ? "0" : answer.join("");
}

console.log(solution([0, 0, 0]));
