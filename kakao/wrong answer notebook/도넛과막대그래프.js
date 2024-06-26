function solution(edges) {
  const answer = new Array(4).fill(0);
  const graph = {};
  // {
  // key: [output, input]
  //   1: [1, 2],
  //   2: [2, 0], => [0,0]
  //   3: [0, 2],
  //   4: [1, 0],
  // };

  // 나가는 간선과 들어오는 간선 등록
  edges.forEach(([a, b]) => {
    if (!graph[a]) {
      graph[a] = [0, 0];
    }
    if (!graph[b]) {
      graph[b] = [0, 0];
    }
    graph[a][0]++;
    graph[b][1]++;
  });

  // 루트노드의 조건은 들어오는 건 없지만 나가는 간선이 두개 이상이면서 최대 간선이여야한다. (그래프는 2개 이상이니깐)
  for (let key in graph) {
    if (graph[key][0] >= 2 && graph[key][1] == 0) {
      answer[0] = Math.max(answer[0], key);
    }
  }

  // 시작하는 정점에서 나가는 간선의 개수
  let total = graph[answer[0]][0];

  for (const [a, b] of edges) {
    // b로 들어오는 루트의 간선을 제거한다.
    if (a !== answer[0]) continue;
    graph[b][1]--;
  }

  for (const key in graph) {
    // key의 나가는 간선이
    if (graph[key][0] == 0 && graph[key][1] >= 0) {
      // 막대그래프는 나가는 간선은 없고 들어오는 간선은 없거나 하나 이상일 때.
      answer[2]++;
      continue;
    } else if (graph[key][0] == 2 && graph[key][1] == 2) {
      // 8자그래프는 나가는 간선 2개 들어오는 간선 2개의 조건이 맞으면.
      answer[3]++;
      continue;
    }
  }

  answer[1] = total - answer[2] - answer[3];
  return answer;
}

console.log(
  solution([
    [2, 3],
    [4, 3],
    [1, 1],
    [2, 1],
  ])
);

// 도넛 모양은 탐색을 시작하여 자기 자신으로 돌아오게 될 경우에 가지는 모양
// 막대그래프는 나가는 간선은 없고 들어오는 간선은 없거나 하나 이상일 때.
// 8자그래프는 나가는 간선 2개 들어오는 간선 2개의 조건이 맞으면.
