function solution(new_id = "") {
  let resultId = new_id
    .toLowerCase()
    .replace(/[^a-z0-9-_.]/g, "")
    .replace(/\.{2,}/g, ".")
    .replace(/^\.|\.$/g, "");

  if (resultId.length == 0) {
    resultId = "a";
  }
  if (resultId.length >= 16) {
    resultId = resultId.slice(0, 15).replace(/\.$/g, "");
  }

  if (resultId.length <= 2) {
    const char = resultId[resultId.length - 1];
    while (resultId.length < 3) {
      resultId += char;
    }
  }
  return resultId;
}

console.log(solution("z-+.^."));
