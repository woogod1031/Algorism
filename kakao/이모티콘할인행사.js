function solution(users = [], emoticons = []) {
  const answer = [0, 0];
  const discount = [10, 20, 30, 40];
  const arr = [];

  function dfs(emts, result) {
    if (emts.length < 1) {
      arr.push(result);
      return;
    }

    for (let i = 0; i < discount.length; i++) {
      dfs(emts.slice(1), [...result, [discount[i], emts[0]]]);
    }
  }
  function discounting(dis, price) {
    return ((100 - dis) / 100) * price;
  }

  dfs(emoticons, []);
  console.log(arr);
  arr.forEach((disArr) => {
    const accrue = [0, 0];

    users.forEach(([per, price]) => {
      let sum = 0;
      disArr.forEach(([dis, cost]) => {
        // 사용자 dis 이상값만
        if (dis >= per) {
          sum += discounting(dis, cost);
        }
      });
      if (sum >= price) {
        accrue[0] += 1;
      } else {
        accrue[1] += sum;
      }
    });

    if (answer[0] < accrue[0]) {
      answer[0] = accrue[0];
      answer[1] = accrue[1];
    } else if (answer[0] == accrue[0]) {
      if (answer[1] < accrue[1]) {
        answer[1] = accrue[1];
      }
    }
  });
  return answer;
}

solution(
  [
    [40, 2900],
    [23, 10000],
    [11, 5200],
    [5, 5900],
    [40, 3100],
    [27, 9200],
    [32, 6900],
  ],
  [1300, 1500, 1600, 4900]
);
