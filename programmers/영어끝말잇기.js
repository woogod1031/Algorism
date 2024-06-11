function solution(n, words) {
  const map = new Map();

  // 시작 세팅
  let circul = 1;
  let playerIndex = 0;
  let before_word = words.shift();
  map.set(before_word, 1);

  // words를 순회한다.
  while (words.length > 0) {
    // 한바퀴를 다 돌면 circul을 +1해준다
    if (playerIndex + 1 == n) {
      circul += 1;
      playerIndex = (playerIndex + 1) % n;
    } else {
      playerIndex += 1;
    }

    const current_word = words.shift();

    // 이전 단어의 마지막과 현재 단어의 맨 처음을 비교
    if (before_word.at(-1) !== current_word.at(0)) {
      return [playerIndex + 1, circul];
    }
    // map에 현재 단어가 있는지 확인
    if (map.has(current_word)) return [playerIndex + 1, circul];
    before_word = current_word;
    map.set(current_word, 1);
  }

  return [0, 0];
}

console.log(
  solution(3, [
    "tank",
    "kick",
    "know",
    "wheel",
    "land",
    "dream",
    "mother",
    "robot",
    "tank",
  ])
);
