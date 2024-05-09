function solution(s) {
  const string = s.replace(/{/g, "[").replace(/}/g, "]");
  const tuple = JSON.parse(string).sort((a, b) =>
    a.length > b.length ? 1 : a.length < b.length ? -1 : 0
  );
  const answer = [];
  tuple.forEach((arr) => {
    arr.forEach((a) => {
      if (answer.some((b) => a == b)) return;
      return answer.push(a);
    });
  });
  return answer;
}

console.log(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"));
