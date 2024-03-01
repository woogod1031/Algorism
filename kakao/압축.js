function solution(msg) {
  const indexArr = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
  ];
  const arr = msg.split("");
  const result = [];

  while (arr.length) {
    let char = "";
    const len = arr.length;
    for (let i = 0; i < len; i++) {
      if (indexArr.includes(char + arr[0])) {
        char += arr.shift();
        continue;
      }
      break;
    }
    if (arr.length) {
      indexArr.push(char + arr[0]);
    }
    const index = indexArr.indexOf(char);
    result.push(index + 1);
  }
  return result;
}

console.log(solution("TOBEORNOTTOBEORTOBEORNOT"));
// TO   BEORNOTTOBEORTOBEORNOT
// console.log(solution("KAKAO"));
