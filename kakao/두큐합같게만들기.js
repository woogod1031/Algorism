function solution(queue1, queue2) {
  let result = 0;
  const array = [...queue1, ...queue2];
  let len = queue1.length;
  let q1 = 0;
  let q2 = len;
  let sum = queue1.reduce((ac, cu) => ac + cu);
  let target = array.reduce((ac, cu) => ac + cu) / 2;

  for (let i = 0; i < len * 3; i++) {
    if (sum == target) {
      return result;
    }
    if (sum < target) {
      sum += array[q2];
      q2 += 1;
    } else if (sum > target) {
      sum -= array[q1];
      q1 += 1;
    }
    result += 1;
  }
  return -1;
}

solution([3, 2, 7, 2], [4, 6, 5, 1]);
