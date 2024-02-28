function solution(friends, gifts = []) {
  const len = friends.length;
  const friendsGraph = {};
  const giftGraph = new Array(len).fill(0).map(() => new Array(len).fill(0));
  const rankInfo = new Array(len).fill(0);
  const nextMonth = new Array(len).fill(0);

  friends.forEach((e, i) => {
    friendsGraph[e] = i;
  });

  gifts.forEach((e, i) => {
    const [a, b] = e.split(" ");
    giftGraph[friendsGraph[a]][friendsGraph[b]]++;
  });

  for (let i = 0; i < len; i++) {
    rankInfo[i] = giftGraph[i].reduce((acc, cur) => (acc += cur), 0);
    for (let j = 0; j < len; j++) {
      rankInfo[i] -= giftGraph[j][i];
    }
  }

  for (let i = 0; i < len; i++) {
    for (let j = i + 1; j < len; j++) {
      if (i == j) continue;
      if (giftGraph[i][j] > giftGraph[j][i]) nextMonth[i]++;
      if (giftGraph[i][j] < giftGraph[j][i]) nextMonth[j]++;
      if (giftGraph[i][j] == giftGraph[j][i]) {
        if (rankInfo[i] > rankInfo[j]) nextMonth[i]++;
        if (rankInfo[i] < rankInfo[j]) nextMonth[i]++;
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
