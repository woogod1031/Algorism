function solution(gems) {
  const set = new Set(gems);
  let result = [0, 99999];

  gems.forEach((_, index) => {
    const s = new Set();

    inner: for (let i = index; i < gems.length; i++) {
      if (s.has(gems[i])) {
        continue;
      } else {
        s.add(gems[i]);

        if (s.size == set.size) {
          if (i - index < result[1] - result[0]) {
            result = [index + 1, i + 1];
          }
          break inner;
        }
      }
    }
  });

  return [result[0], result[1]];
}

console.log(
  solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])
);
