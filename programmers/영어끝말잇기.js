function solution(n, words) {
  // 시작 세팅
  const set = new Set();
  set.add(words.at(0));

  // words의 개수만큼 반복한다.
  for (let i = 1; i < words.length; i++) {
    const current_word = words.at(i);

    // map에 현재 단어가 있는지 확인 또는 이전 단어의 마지막과 현재 단어의 맨 처음을 비교
    if (set.has(current_word) || words.at(i - 1).at(-1) !== words[i].at(0))
      return [(i % n) + 1, Math.ceil((i + 1) / n)];
    set.add(current_word);
  }

  return [0, 0];
}

console.log(
  solution(2, ["hello", "one", "even", "never", "now", "world", "draw"])
);
