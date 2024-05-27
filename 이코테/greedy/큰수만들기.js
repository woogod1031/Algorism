function solution(number, k) {
  const numbers = number.split("");
  const stack = [];

  numbers.forEach((v, i, o) => {
    while (v > stack[stack.length - 1] && k > 0) {
      stack.pop();
      k -= 1;
    }
    stack.push(v);
  });

  const result = stack.slice(0, stack.length - k);
  return result.join("");
}
