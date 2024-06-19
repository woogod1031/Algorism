// 내 풀이

function getCombination(array, level) {
  if (level == 0) return array.map((v) => [v]);

  const result = array.flatMap((key, index) => {
    const rest_combi = getCombination(array.slice(index + 1), level - 1);
    const combination = rest_combi.map((v) => [key, ...v]);
    return combination;
  });

  return result;
}

function solution(relation) {
  const keys = new Array(relation[0].length).fill(0).map((_, i) => i); // [0,1,2,3]
  const key_combination = keys.flatMap((key_index) =>
    getCombination(keys.slice(), key_index)
  );

  const set = new Set();
  const result = key_combination.filter((_keys) => {
    // 해당 키가 유일성을 가지나요?
    const _set = new Set();
    if (
      relation.every((rel) => {
        const el = _keys.map((key) => rel[key]).join(",");
        if (_set.has(el)) return false;
        _set.add(el);
        return true;
      })
    ) {
      // 해당 키가 최소성에 해당하나요?
      const new_keys = _keys.flatMap((_, _index) =>
        getCombination(_keys.slice(), _index)
      );
      if (new_keys.length && new_keys.every((key) => !set.has(key.join(",")))) {
        set.add(_keys.join(","));
        return true;
      }
    }
    return false;
  });
  return result.length;
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
