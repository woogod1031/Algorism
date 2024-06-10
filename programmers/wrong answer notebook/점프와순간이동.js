function solution(n) {
  let result = 1;
  let num = n;

  while (num > 1) {
    if (num % 2 == 0) {
      num /= 2;
    } else {
      num -= 1;
      result += 1;
    }
  }

  return result;
}

// dp 풀이법, 효율성 0점

// function solution(n) {
//   const dp = new Array(n + 1).fill(0);

//   dp[1] = 1;

//   for (let i = 2; i < n + 1; i++) {
//     if (i % 2 == 0) {
//       dp[i] = Math.min(dp[i / 2], dp[i - 1] + 1);
//     } else {
//       dp[i] = Math.min(dp[i - 1] + 1);
//     }
//   }
//   return dp[n];
// }
