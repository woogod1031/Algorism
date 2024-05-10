function solution(record = []) {
  const map = new Map();

  record.forEach((cu) => {
    const [method, _id, _name] = cu.split(" ");
    if (method == "Enter" || method == "Change") map.set(_id, _name);
  });

  const answer = [];
  record.forEach((cu) => {
    const [method, _id, _name] = cu.split(" ");
    const newId = map.get(_id);
    if (method == "Enter") answer.push(`${newId}님이 들어왔습니다.`);
    if (method == "Leave") answer.push(`${newId}님이 나갔습니다.`);
  });
  return answer;
}

solution([
  "Enter uid1234 Muzi",
  "Enter uid4567 Prodo",
  "Leave uid1234",
  "Enter uid1234 Prodo",
  "Change uid4567 Ryan",
]);
