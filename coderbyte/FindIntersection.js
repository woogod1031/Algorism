function FindIntersection(strArr) {
  const array = strArr.flatMap((str) => str.split(", "));
  const map = {};
  array.forEach((v) => {
    if (map[v]) map[v] = map[v] + 1;
    else map[v] = 1;
  });
  const result = Object.entries(map).filter(([k, v]) => v >= 2);
  if (result.length == 0) return false;
  return result.map(([k, v]) => k);
}

console.log(FindIntersection(["1, 3, 9, 10, 17, 18", "1, 4, 9, 10"]));
