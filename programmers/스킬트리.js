// 내 정답

function solution(skill, skill_trees) {
  const skillMap = new Map();
  // skillMap 세팅: 스킬트리 순서가 있다.
  skill.split("").forEach((value, index) => {
    skillMap.set(value, index);
  });

  // 가능한 것들만 필터링.
  const possibles = skill_trees.filter((tree) => {
    // tree를 배열로
    tree = tree.split("");

    // Arr으로 현재 스킬트리 스킬들 저장
    const array = [];

    for (value of tree) {
      // 아닌 건 관련없음
      if (skillMap.has(value)) {
        const current = skillMap.get(value);
        // current가 첫번째면 push
        if (current == 0) {
          array.push(value);
        }
        // array에 스킬들이 존재할 때, array 최근 요소가 바로 전 단계면
        else if (
          array.length !== 0 &&
          current - 1 == skillMap.get(array.at(-1))
        ) {
          array.push(value);
        } else {
          return false;
        }
      }
    }
    return true;
  });

  return possibles.length;
}

// 다른 사람 정답
// function solution(skill, skill_trees) {
//   // skill(C,B,D)을 제외한 문자를 match
//   // const regex = new RegExp(`[^${skill}]`, "g");
//   // 그럼 CBD만 남게 된다.
//   // tree.replace(regex, '')
//   // 여기서 매칭되는거(indexof(x) === 0) 혹은 없는 경우 "" 만 통과
//   // return skill.indexOf(x) === 0 || x === "";

//   return skill_trees.filter((tree) => {
//     const test = skill.split(""); // ["C","B","D"]
//     for (let i = 0; i < tree.length; i++) {
//       if (!skill.includes(tree[i])) continue;
//       if (tree[i] === test.shift()) continue;
//       return false;
//     }
//     return true;
//   }).length;
// }

console.log(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]));
