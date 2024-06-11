const dx = [1, 0, -1];
const dy = [0, 1, -1];

function solution(n) {
  if (n == 1) return [1];
  let max = 0;

  const arr = new Array(n).fill(0).map((_, i) => {
    max += i + 1;
    return new Array(i + 1).fill(0);
  });

  let current = [0, 0];
  let path = 0;

  for (let i = 1; i <= max; i++) {
    const [x, y] = current;
    arr[x][y] = i;

    const nx = x + dx[path];
    const ny = y + dy[path];

    if (nx < 0 || ny < 0 || nx >= n || ny >= arr[nx].length) {
      path = (path + 1) % 3;
      const nnx = x + dx[path];
      const nny = y + dy[path];
      current = [nnx, nny];
    } else {
      if (arr[nx][ny] !== 0) {
        path = (path + 1) % 3;
        const nnx = x + dx[path];
        const nny = y + dy[path];
        current = [nnx, nny];
      } else {
        current = [nx, ny];
      }
    }
  }
  return arr.reduce((a, c) => [...a, ...c], []);
}

// function solution(n) {
//   if (n == 1) return [1];

//   // 반복 최대 개수, 층별 배열 구현
//   let max = 0;
//   const arr = new Array(n).fill(0).map((_, i) => {
//     max += i + 1;
//     return new Array(i + 1).fill(0);
//   });

//   let number = 0; // 할당할 숫자
//   let current = [0, 0]; // 현재 위치
//   let method = 0; // 현재 방향 지정

//   // 0부터 max전까지만 구한다.
//   for (let i = 0; i < max; i++) {
//     const [x, y] = current;
//     number += 1;
//     arr[x][y] = number;
//     const _nx = x + dx[method];
//     const _ny = y + dy[method];

//     // 필드 바깥으로 나가는 값을 구한다.
//     if (_nx >= n || _nx < 0 || _ny >= arr[_nx].length || _ny < 0) {
//       const n_method = (method + 1) % 3;
//       const __nx = x + dx[n_method];
//       const __ny = y + dy[n_method];

//       // 1을 제외하고 방향을 변경할 시 바깥으로 나가지 않는 선에서 다음 위치를 구할 수 있기 때문에 0인지만 체크해주면 된다.
//       if (arr[__nx][__ny] == 0) {
//         current = [__nx, __ny];
//         method = n_method;
//         continue;
//       }
//       break;
//     } else {
//       if (arr[_nx][_ny] == 0) {
//         current = [_nx, _ny];
//         continue;
//       } else {
//         const n_method = (method + 1) % 3;
//         const __nx = x + dx[n_method];
//         const __ny = y + dy[n_method];
//         if (__nx >= n || __nx < 0 || __ny >= arr[__nx].length || __ny < 0) {
//           break;
//         } else if (arr[__nx][__ny] == 0) {
//           current = [__nx, __ny];
//           method = n_method;
//           continue;
//         }
//       }
//     }
//   }

//   // 재귀에 묶이지 않아도 되는 문제였다.
//   // dfs가 단순히 또 하나의 dfs를 호출하는 방식이라 분기가 되지 않기에, for문으로 구성해도 좋았을 문제

//   // function trace(current, method) {
//   //   const [x, y] = current;
//   //   number += 1;
//   //   arr[x][y] = number;

//   //   const _nx = x + dx[method];
//   //   const _ny = y + dy[method];

//   //   if (_nx >= n || _nx < 0 || _ny >= arr[_nx].length || _ny < 0) {
//   //     const n_method = (method + 1) % 3;
//   //     const __nx = x + dx[n_method];
//   //     const __ny = y + dy[n_method];
//   //     if (arr[__nx][__ny] == 0) trace([__nx, __ny], n_method);
//   //   } else {
//   //     if (arr[_nx][_ny] == 0) {
//   //       trace([_nx, _ny], method);
//   //     } else {
//   //       const n_method = (method + 1) % 3;
//   //       const __nx = x + dx[n_method];
//   //       const __ny = y + dy[n_method];
//   //       if (__nx >= n || __nx < 0 || __ny >= arr[__nx].length || __ny < 0) {
//   //       } else if (arr[__nx][__ny] == 0) trace([__nx, __ny], n_method);
//   //     }
//   //   }
//   // }

//   // trace([0, 0], 0);

//   // 층별 총합 후 반환
//   return arr.reduce((a, c) => [...a, ...c], []);
// }

console.log(solution(6));
