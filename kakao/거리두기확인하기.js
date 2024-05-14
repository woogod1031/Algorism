function solution(places) {
  places = places.map((place) => place.map((p) => p.split("")));
  const dx = [0, 0, 1, -1];
  const dy = [1, -1, 0, 0];

  function check(positions, _map) {
    return positions.some((pos, i) => {
      const [x, y] = pos;
      return positions.some((_pos, _i) => {
        if (i == _i) return false;
        const [_x, _y] = _pos;
        if (Math.abs(x - _x) + Math.abs(y - _y) > 2) {
          return false;
        } else {
          for (let i = 0; i < 4; i++) {
            const nx = x + dx[i];
            const ny = y + dy[i];
            if (nx >= 0 && nx < 5 && ny >= 0 && ny < 5) {
              if (_map[nx][ny] == "P") return true;
              if (_map[nx][ny] == "O") {
                for (let j = 0; j < 4; j++) {
                  const nnx = nx + dx[j];
                  const nny = ny + dy[j];
                  if (nnx >= 0 && nnx < 5 && nny >= 0 && nny < 5) {
                    if (nnx !== x || nny !== y) {
                      if (_map[nnx][nny] === "P") {
                        return true;
                      }
                    }
                  }
                }
                return false;
              }
            }
          }
          return false;
        }
      });
    });
  }

  const answer = places.map((map) => {
    let _positions = [];
    map.forEach((x, x_idx) => {
      x.forEach((y, y_idx) => {
        if (y == "P") {
          _positions.push([x_idx, y_idx]);
        }
      });
    });

    if (_positions.length <= 1 || !check(_positions, map)) {
      return 1;
    }
    return 0;
  });

  return answer;
}

console.log(
  solution([
    ["POOOO", "XPOOO", "OOOOO", "OOOOO", "OOOOO"],
    ["OOOOO", "OOOOO", "OOOOO", "OOOOO", "OOOOO"],
    ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
  ])
);
