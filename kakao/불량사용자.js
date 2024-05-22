function getCombinations(arrays) {
  const result = [];
  const set = new Set();

  function rc(arr, index) {
    if (index == arrays.length) {
      const combi = arr.slice().sort().join(",");
      if (!set.has(combi)) {
        result.push([...arr]);
        set.add(combi);
      }
      return;
    }
    for (let i = 0; i < arrays[index].length; i++) {
      if (arr.includes(arrays[index][i])) continue;
      arr.push(arrays[index][i]);
      rc(arr, index + 1);
      arr.pop();
    }
  }

  rc([], 0);
  return result;
}

function solution(user_id, banned_id) {
  const arrays = [];

  banned_id.forEach((bid) => {
    const arr = user_id.filter((uid) => {
      if (uid.length !== bid.length) return false;
      for (let i = 0; i < uid.length; i++) {
        if (uid[i] !== bid[i]) {
          if (bid[i] == "*") continue;
          return false;
        }
      }
      return true;
    });
    arrays.push(arr);
  });
  const combinations = getCombinations(arrays);
  return combinations.length;
}

console.log(
  solution(
    ["frodo", "fradi", "crodo", "abc123", "frodoc"],
    ["*rodo", "*rodo", "******"]
  )
);
