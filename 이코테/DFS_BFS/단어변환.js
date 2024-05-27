function checkDiff(o, a) {
  const ori_arr = o.split("");
  const ano_arr = a.split("");
  const result = [];

  for (let i = 0; i < ori_arr.length; i++) {
    if (ori_arr[i] !== ano_arr[i]) {
      result.push([ano_arr[i], i]);
    }
  }
  return result;
}

function solution(begin, target, words) {
  const ii = words.indexOf(target);
  if (ii == -1) return 0;

  let level = 1e9;
  let visited = new Array(words.length).fill(0).map((_, i) => {
    if (i == ii) return true;
    return false;
  });

  function dfs(word, count) {
    if (checkDiff(word, begin).length == 1) {
      level = Math.min(level, count + 1);
    } else {
      for (let i = 0; i < words.length; i++) {
        if (visited[i]) continue;
        const arr = checkDiff(word, words[i]);
        if (arr.length == 1) {
          const [wd, idx] = arr.pop();
          const word_arr = word.split("");
          word_arr.splice(idx, 1, wd);
          visited[i] = true;
          dfs(word_arr.join(""), count + 1);
          visited[i] = false;
        }
      }
    }
    if (checkDiff(word, begin).length == 1) {
      level = Math.min(level, count + 1);
    }
  }
  dfs(target, 0);

  if (level == 1e9) {
    return 0;
  } else {
    return level;
  }
}

console.log(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]));
