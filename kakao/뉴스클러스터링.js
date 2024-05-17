function getSimiler(map1 = new Map(), map2 = new Map()) {
  const array = [
    ...new Set(
      Array.from(map1, ([key]) => key).concat(
        ...Array.from(map2, ([key]) => key)
      )
    ),
  ];

  let union = 0;
  let cross = 0;

  array.forEach((v) => {
    if (map1.has(v) && map2.has(v)) {
      union += Math.max(map1.get(v), map2.get(v));
      cross += Math.min(map1.get(v), map2.get(v));
    } else {
      if (map1.has(v)) {
        union += map1.get(v);
      } else {
        union += map2.get(v);
      }
    }
  });

  const simility = union == 0 && cross == 0 ? 1 : cross / union;
  const result = Math.floor(simility * 65536);

  return result;
}

function getMap(string) {
  string = string.toLowerCase();
  const map = new Map();
  const regex = /[0-9\s\W\d_]/;

  for (let i = 1; i < string.length; i++) {
    const target = string[i - 1] + string[i];

    if (regex.test(target)) continue;

    if (map.has(target)) {
      map.set(target, map.get(target) + 1);
    } else {
      map.set(target, 1);
    }
  }

  return map;
}

function solution(str1, str2) {
  str1 = getMap(str1);
  str2 = getMap(str2);

  const answer = getSimiler(str1, str2);

  return answer;
}

console.log(solution("handshake", "shake hands"));
