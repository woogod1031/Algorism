function solution(k, dungeons) {
  let result = 0;
  let visited = Array(dungeons.length)
    .fill(0)
    .map(() => false);

  function dfs(least, count) {
    if (count <= 0) {
      result = Math.max(result, visited.filter((v) => v).length);
    } else {
      for (let i = 0; i < dungeons.length; i++) {
        if (visited[i]) continue;
        const newCount = count - 1;
        if (least >= dungeons[i][0]) {
          visited[i] = true;
          dfs(least - dungeons[i][1], newCount);
          visited[i] = false;
        } else {
          continue;
        }
      }
    }
    result = Math.max(result, visited.filter((v) => v).length);
  }
  dfs(k, dungeons.length);
  return result;
}

console.log(
  solution(80, [
    [80, 20],
    [50, 40],
    [30, 10],
  ])
);
