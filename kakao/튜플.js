function solution(s) {
  let str = "";
  for (char of s) {
    if (char == "{") char = "[";
    if (char == "}") char = "]";
    str += char;
  }
  const array = JSON.parse(str);
  array.sort((a, b) => a.length - b.length);

  let set = new Set();
  array.forEach((ar) => {
    ar.forEach((v) => {
      if (!set.has(v)) set.add(v);
    });
  });
  return [...set.values()];
}

console.log(solution("{{123}}"));
