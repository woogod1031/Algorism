function solution(friends, gifts) {
  const len = friends.length;
  const friendsGraph = new Map();
  const giftsGraph = new Array(len).fill(0).map(() => new Array(len).fill(0));
  const rankInfo = new Array(len).fill(0);
  const nextMonth = new Array(len).fill(0);

  friends.forEach((name, idx) => {
    friendsGraph.set(name, idx);
  });

  gifts.forEach((info) => {
    const [a, b] = info.split(" ");
    giftsGraph[friendsGraph.get(a)][friendsGraph.get(b)]++;
  });

  for (let i = 0; i < len; i++) {
    rankInfo[i] = giftsGraph[i].reduce((acc, cur) => (acc += cur), 0);

    for (let j = 0; j < len; j++) {
      rankInfo[i] -= giftsGraph[j][i];
    }
  }

  for (let i = 0; i < len; i++) {
    for (let j = i + 1; j < len; j++) {
      if (j == i) continue;
      if (giftsGraph[i][j] > giftsGraph[j][i]) nextMonth[i]++;
      if (giftsGraph[i][j] < giftsGraph[j][i]) nextMonth[j]++;
      if (giftsGraph[i][j] === giftsGraph[j][i]) {
        if (rankInfo[i] > rankInfo[j]) nextMonth[i]++;
        if (rankInfo[i] < rankInfo[j]) nextMonth[j]++;
      }
    }
  }
  return Math.max(...nextMonth);
}

console.log(
  solution(
    ["muzi", "ryan", "frodo", "neo"],
    [
      "muzi frodo",
      "muzi frodo",
      "ryan muzi",
      "ryan muzi",
      "ryan muzi",
      "frodo muzi",
      "frodo ryan",
      "neo muzi",
    ]
  )
);
