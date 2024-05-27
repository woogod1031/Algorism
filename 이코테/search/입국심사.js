function solution(n, times) {
  let left = 1;
  let right = Math.max(...times) * n;
  let result = 0;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    const temp = times.reduce((acc, cur) => (acc += Math.floor(mid / cur)), 0);

    if (temp >= n) {
      right = mid - 1;
      result = mid;
    }
    if (temp < n) {
      left = mid + 1;
    }
  }
  return result;
}

solution(6, [7, 10]);
