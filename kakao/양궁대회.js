function scoreCheck(ryan, apeach) {
  let rscore = 0;
  let ascore = 0;

  for (let i = 0; i < ryan.length; i++) {
    if (ryan[i] == 0 && apeach[i] == 0) continue;
    if (ryan[i] > apeach[i]) {
      rscore += 10 - i;
    } else {
      ascore += 10 - i;
    }
  }
  return rscore - ascore;
}

function solution(n, info = []) {
  let answer = [-1];
  const apeachScore = info.slice();
  let ryanScore = Array(info.length).fill(0);
  let check = 0;

  function dfs(count) {
    if (count < 0) return;
    if (count == 0) {
      let newCheck = scoreCheck(ryanScore, apeachScore);
      if (newCheck >= check && newCheck !== 0) {
        check = newCheck;
        answer = ryanScore.slice();
      }
    }

    for (let i = 0; i < apeachScore.length; i++) {
      if (ryanScore[i] - apeachScore[i] >= 1) return; // (10-i)점을 ryan이 가져간 경우
      if (apeachScore[i] >= ryanScore[i]) {
        let lion_arrows = apeachScore[i] + 1;
        ryanScore[i] += lion_arrows;
        dfs(count - lion_arrows);
        if (count - lion_arrows >= 0) {
          ryanScore[10] += count - lion_arrows;
          dfs(0);
          ryanScore[10] -= count - lion_arrows;
        }
        ryanScore[i] -= lion_arrows;
      }
    }
  }

  dfs(n);
  return answer;
}

console.log(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]));
