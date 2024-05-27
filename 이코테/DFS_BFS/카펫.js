function solution(brownCnt, yellowCnt) {
  const combinations = [];
  for (let i = 1; i < brownCnt + 1; i++) {
    const width = i / 2;
    if (width % 1 !== 0) continue;

    const height = (brownCnt - 2 * width) / 2 + 2;
    if (width == height || width >= height) {
      combinations.push([width, height]);
    }
  }

  for (let c of combinations) {
    const yelloRec = (c[0] - 2) * (c[1] - 2);
    if (yelloRec == yellowCnt) return [c[0], c[1]];
  }
}

solution(24, 24);
