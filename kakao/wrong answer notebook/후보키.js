// 콤비네이션 제작 참고

function getCombination(array, level) {
  if (level == 1) return array.map((v) => [v]);

  const result = [];
  for (let i = 0; i < array.length; i++) {
    const key = array[i];
    const rest = array.slice(i + 1);
    const combi = getCombination(rest, level - 1).map((com) => [key, ...com]);
    result.push(...combi);
  }
  return result;
}

function solution(relation) {
  const key_array = new Array(relation[0].length).fill(0).map((_, i) => i); // [0,1,2,3]
  const key_combination = [];

  for (let i = 0; i < key_array.length; i++) {
    key_combination.push(...getCombination(key_array, i + 1));
  }

  const key_set = new Set(); // "0", "1,2"

  key_combination.forEach((key) => {
    // 성립 되는지 체크
    const set = new Set();
    const isCorrect = relation.every((item) => {
      const value = key.map((v) => item[v]).join();
      if (set.has(value)) return false;
      set.add(value);
      return true;
    });

    if (isCorrect) {
      let result = [];

      for (let i = 0; i < key.length; i++) {
        result.push(...getCombination(key, i + 1));
      }

      if (result.every((v) => !key_set.has(v.join()))) {
        key_set.add(key.join());
      }
    }
  });

  return key_set.size;
}

console.log(
  solution([
    ["100", "ryan", "music", "2"],
    ["200", "apeach", "math", "2"],
    ["300", "tube", "computer", "3"],
    ["400", "con", "computer", "4"],
    ["500", "muzi", "music", "3"],
    ["600", "apeach", "music", "2"],
  ])
);
