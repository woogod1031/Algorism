function solution(n, t, m, p) {
  // t가 나올때까지 m을 뺑뺑이를 돌린다.
  let t_cnt = 0;
  let text = "";
  let count = 0;

  function toNary(num) {
    return num.toString(n);
  }

  let count_arr = toNary(count).split("");

  while (t_cnt !== t) {
    for (let i = 1; i < m + 1; i++) {
      if (i == p) {
        t_cnt += 1;
        text += count_arr.shift();
      } else {
        count_arr.shift();
      }

      if (!count_arr.length) {
        count += 1;
        count_arr = toNary(count).split("");
      }
    }
  }

  text = text.toUpperCase();
  return text;
}

console.log(solution(16, 16, 2, 2));
