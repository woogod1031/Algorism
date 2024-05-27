const dx = [1, -1, 0, 0];
const dy = [0, 0, 1, -1];

function solution(rectangle, characterX, characterY, itemX, itemY) {
  characterX *= 2;
  characterY *= 2;
  itemX *= 2;
  itemY *= 2;
  let dobuleRec = rectangle.map((rec) => rec.map((point) => point * 2));
  const start = [characterX, characterY, 0];
  let que = [start];
  let range = new Array(103).fill(0).map(() => new Array(103).fill(0));

  dobuleRec.forEach(([x1, y1, x2, y2]) => {
    for (let i = x1; i <= x2; i++) {
      for (let j = y1; j <= y2; j++) {
        if (i == x1 || i == x2 || j == y1 || j == y2) {
          if (range[i][j] == 0) range[i][j] = 1;
        } else {
          range[i][j] = 2;
        }
      }
    }
  });

  range[characterX][characterY] = 0;

  while (que.length) {
    let [x, y, c] = que.shift();
    if (x == itemX && y == itemY) return c / 2;

    for (let i = 0; i < 4; i++) {
      let chX = x + dx[i];
      let chY = y + dy[i];
      if (range[chX][chY] == 1) {
        que.push([chX, chY, c + 1]);
        range[chX][chY] = 0;
      }
    }
  }
  return 0;
}

solution(
  [
    [1, 1, 7, 4],
    [3, 2, 5, 5],
    [4, 3, 6, 9],
    [2, 6, 8, 8],
  ],
  1,
  3,
  7,
  8
);
