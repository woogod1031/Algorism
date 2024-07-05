function solution(prices) {
  const answer = prices.map((v, i) => {
    let a = 0;

    for (let j = i + 1; j < prices.length; j++) {
      if (v > prices[j]) return a + 1;
      a += 1;
    }
    return a;
  });
  return answer;
}

// 스택 활용 풀이/ 효율성은 더 괜찮았음
// function solution(prices) {
//   const answer = new Array(prices.length).fill(0);
//   const stack = [];
//   let length = prices.length;

//   for (let i = 0; i < length; i++) {
//     while (stack.length && prices[i] < prices[stack[stack.length - 1]]) {
//       let temp = stack.pop();
//       answer[temp] = i - temp;
//     }
//     stack.push(i);
//   }

//   while (stack.length) {
//     let temp = stack.pop();
//     answer[temp] = length - temp - 1;
//   }

//   return answer;
// }

// console.log(solution([1, 2, 3, 2, 3]));
