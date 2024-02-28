function solution(id_list, report, k) {
  const len = id_list.length;
  const idMap = new Map();
  const reportGraph = new Array(len).fill(0).map(() => new Array(len).fill(0));
  id_list.forEach((id, idx) => idMap.set(id, idx));
  report.forEach((res) => {
    const [from, to] = res.split(" ");
    if (reportGraph[idMap.get(from)][idMap.get(to)] < 1) {
      reportGraph[idMap.get(from)][idMap.get(to)]++;
    }
  });
  const resultGraph = new Array(len).fill(0);
  for (let i = 0; i < len; i++) {
    reportGraph[i].forEach((e, idx) => (resultGraph[idx] += e));
  }
  const mailGraph = new Array(len).fill(0);
  for (let i = 0; i < len; i++) {
    if (resultGraph[i] >= k) {
      for (let j = 0; j < len; j++) {
        if (reportGraph[j][i] >= 1) {
          mailGraph[j] += 1;
        }
      }
    }
  }

  return mailGraph;
}

solution(
  ["muzi", "frodo", "apeach", "neo"],
  ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
  2
);
