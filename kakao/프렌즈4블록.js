function solution(m, n, board) {
  board = board.map((s) => s.split(""));

  while (true) {
    let deleted_list = [];

    for (let i = 1; i < m; i++) {
      for (let j = 1; j < n; j++) {
        if (
          board[i][j] &&
          board[i][j] === board[i][j - 1] &&
          board[i][j] === board[i - 1][j - 1] &&
          board[i][j] === board[i - 1][j]
        ) {
          deleted_list.push([i, j]);
        }
      }
    }

    if (!deleted_list.length)
      return [].concat(...board).filter((v) => !v).length;

    deleted_list.forEach(([x, y]) => {
      board[x][y] = 0;
      board[x][y - 1] = 0;
      board[x - 1][y - 1] = 0;
      board[x - 1][y] = 0;
    });

    for (let i = m - 1; i > 0; i--) {
      if (board[i].every((v) => v)) continue;
      for (let j = 0; j < n; j++) {
        // (i,j)값이 비어있을 때, k값(j줄의 상단에 위치한 값)을 가져온다.
        for (let k = i - 1; k >= 0 && !board[i][j]; k--) {
          if (board[k][j]) {
            board[i][j] = board[k][j];
            board[k][j] = 0;
            break;
          }
        }
      }
    }
  }
}

console.log(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]));
