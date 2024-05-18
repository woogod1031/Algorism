function getGCD(num1, num2) {
  let gcd = 1;

  for (let i = 2; i <= Math.min(num1, num2); i++) {
    if (num1 % i === 0 && num2 % i === 0) {
      gcd = i;
    }
  }

  return gcd;
}

function solution(w, h) {
  let gcd = getGCD(w, h);

  let answer = w * h - (w + h - gcd);
  return answer;
}

solution(8, 12);
