function isPrime(num) {
  if (num === 1) return false;

  for (let i = 2; i < Math.sqrt(num + 1); i++) {
    if (num % i === 0) return false;
  }
  return true;
}

function solution(n, k) {
  n = n.toString(k).split("0");

  const result = n.filter((v) => {
    if (v == "" || !isPrime(+v)) {
      return false;
    }
    return true;
  });
  return result.length;
}

console.log(solution(437674, 3));
