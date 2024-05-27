function solution(tickets) {
  let answer = [];
  const result = [];
  const visited = [];

  tickets.sort();

  const len = tickets.length;

  function dfs(start, cnt) {
    result.push(start);

    if (cnt == len) {
      answer = result;
      return true;
    }

    for (let i = 0; i < len; i++) {
      if (tickets[i][0] === start && !visited[i]) {
        visited[i] = true;
        if (dfs(tickets[i][1], cnt + 1)) return true;
        visited[i] = false;
      }
    }

    result.pop();
    return false;
  }

  dfs("ICN", 0);

  return answer;
}

console.log(
  solution([
    ["ICN", "JFK"],
    ["HND", "IAD"],
    ["JFK", "HND"],
  ])
);
