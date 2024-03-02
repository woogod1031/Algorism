function solution(n, computers) {
  const networks = [];
  const visited = new Array(n).fill(false);

  for (let i = 0; i < n; i++) {
    if (visited[i]) {
      continue;
    }
    const queue = [i];
    const set = new Set();
    set.add(i);

    while (queue.length) {
      const idx = queue.shift();
      visited[idx] = true;
      const connects = computers[idx];
      for (let j = 0; j < connects.length; j++) {
        if (j == idx || set.has(j) || connects[j] == 0) continue;
        set.add(j);
        queue.push(j);
      }
    }
    networks.push(set);
  }
  return networks.length;
}
