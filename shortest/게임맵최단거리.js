const dx = [1, -1, 0, 0];
const dy = [0, 0, 1, -1];

function solution(maps) {
  let result = maps.length * maps[0].length;
  let check = false;
  function go(map, x, y, num) {
    const new_map = map.map((v) => [...v]);
    new_map[y][x] = 0;

    if (x == map[0].length - 1 && y == map.length - 1) {
      result = Math.min(result, num);
      check = true;
      return;
    }
    for (let i = 0; i < 4; i++) {
      const nx = x + dx[i];
      const ny = y + dy[i];
      if (
        nx < 0 ||
        ny < 0 ||
        nx >= new_map[0].length ||
        ny >= new_map.length ||
        new_map[ny][nx] == 0
      ) {
        continue;
      }
      new_map[ny][nx] = 0;
      go(new_map, nx, ny, num + 1);
    }
  }

  go(maps, 0, 0, 1);
  if (!check) {
    return -1;
  }
  return result;
}

solution([[1], [1]]);
