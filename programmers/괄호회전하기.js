function solution(s) {
  const array = s.split("");
  let count = 0;
  if (array.length % 2 !== 0) return count;

  function isCorrect(ar) {
    ar = ar.slice();
    if (ar[0] == "]" || ar[0] == ")" || ar[0] == "}") return false;
    const stack = [];
    for (let i = 0; i < s.length; i++) {
      const a = ar.shift();
      if ((a == "[") | (a == "{") | (a == "(")) {
        stack.push(a);
      } else if (stack.length && a === "]" && stack[stack.length - 1] === "[") {
        stack.pop();
      } else if (stack.length && a === ")" && stack[stack.length - 1] === "(") {
        stack.pop();
      } else if (stack.length && a === "}" && stack[stack.length - 1] === "{") {
        stack.pop();
      } else {
        return false;
      }
    }

    if (stack.length !== 0) {
      return false;
    }
    return true;
  }

  for (let i = 0; i < s.length; i++) {
    array.push(array.shift());
    if (isCorrect(array)) {
      count += 1;
    }
  }

  return count;
}

console.log(solution("[](){}"));

["[", "{", "(", "}"];
