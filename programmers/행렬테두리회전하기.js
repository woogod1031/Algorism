// 내 풀이

const dx = [0, 1, 0, -1];
const dy = [1, 0, -1, 0];

function solution(rows, columns, queries) {
  const map = new Array(rows).fill(0).map((_, i) =>
    new Array(columns).fill(0).map((__, _i) => {
      return i * columns + _i + 1;
    })
  );

  const result = queries.map((query) => {
    const [x1, y1, x2, y2] = query.map((v) => v - 1);

    // 총 회전 수
    const rotate_cnt = 2 * (x2 - x1 + 1 + y2 - y1 + 1) - 4;

    const init_value = map[x1][y1];

    // 최소값, 임시저장값, 현재위치, 이동경로
    let min = init_value,
      save = init_value,
      current = [x1, y1],
      path = 0;

    // 회전 수행
    for (let i = 0; i < rotate_cnt; i++) {
      const [cx, cy] = current;
      let nx = cx + dx[path];
      let ny = cy + dy[path];

      // nx, ny가 범위를 벗어나면 path 변경 후 수정
      if (nx < x1 || nx > x2 || ny < y1 || ny > y2) {
        path = path + 1;
        nx = cx + dx[path];
        ny = cy + dy[path];
      }

      // swap
      [save, map[nx][ny]] = [map[nx][ny], save];
      // 최소값 구하기
      min = Math.min(min, save);
      // current 이동
      current = [nx, ny];
    }
    return min;
  });
  return result;
}

console.log(
  solution(6, 6, [
    [2, 2, 5, 4],
    [3, 3, 6, 6],
    [5, 1, 6, 3],
  ])
);
