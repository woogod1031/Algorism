function solution(numbers) {
  let index = 0;
  const answer = numbers
    .map((numbers) => String(numbers))
    .sort((a, b) => {
      if (Number(a + b) > Number(b + a)) {
        return -1;
      } else {
        return 1;
      }
    })
    .join("");

  return answer[0] === "0" ? "0" : answer;
}
