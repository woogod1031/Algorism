function solution(n, t, m, p) {
  let text = "";
  let count = 0;
  let count_arr = count.toString(n).split("");

  while (text.length !== t) {
    for (let i = 1; i < m + 1; i++) {
      if (i == p) {
        text += count_arr.shift().toUpperCase();
      } else {
        count_arr.shift();
      }

      if (!count_arr.length) {
        count += 1;
        count_arr = count.toString(n).split("");
      }
    }
  }
  return text;
}

console.log(solution(16, 16, 2, 2));
