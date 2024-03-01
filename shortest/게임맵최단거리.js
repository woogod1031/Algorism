function solution(maps) {
  let dx = [1, -1, 0, 0];
  let dy = [0, 0, 1, -1];
  const queue = [];
  const n = maps[0].length;
  const m = maps.length;

  queue.push([0, 0, 1]);
  maps[0][0] = 0;

  while (queue.length > 0) {
    let size = queue.length;
    for (let i = 0; i < size; i++) {
      let [x, y, num] = queue.shift();
      for (let i = 0; i < 4; i++) {
        const nx = x + dx[i];
        const ny = y + dy[i];
        if (nx >= 0 && nx < n && ny >= 0 && ny < m && maps[ny][nx] == 1) {
          if (nx == n - 1 && ny == m - 1) {
            return num + 1;
          }
          queue.push([nx, ny, num + 1]);
          maps[ny][nx] = 0;
        }
      }
    }
  }
  return -1;
}
solution([[1], [1]]);
