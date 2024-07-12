function ArrayChallenge(arr) {
  let max = arr[0];

  for (let i = 1; i < arr.length; i++) {
    let min = arr[i];
    for (let j = i - 1; j >= 0; j--) {
      min = Math.min(min, arr[j]);
      const compareValue = min * (i - j + 1);
      max = Math.max(max, compareValue);
    }
  }

  return max;
}

console.log(ArrayChallenge([6, 3, 1, 4, 12, 4]));
