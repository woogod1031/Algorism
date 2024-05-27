function generateUniquePermutations(arr) {
  const result = [];
  function permute(current, remaining) {
    if (remaining.length === 0) {
      result.push(current.slice());
      return;
    }

    const used = new Set();

    remaining.forEach((v, i) => {
      if (!used.has(v)) {
        used.add(v);
        const next = current.concat(v);
        const newRemaining = [
          ...remaining.slice(0, i),
          ...remaining.slice(i + 1),
        ];
        permute(next, newRemaining);
      }
    });
  }

  permute([], arr);
  return result;
}

function calc(opers, numbers) {
  return numbers.reduce((acc, cur, i) => {
    switch (opers[i]) {
      case "+":
        return (acc += cur);
      case "-":
        return (acc += cur * -1);
    }
  }, 0);
}

function solution(numbers, target) {
  let result = 0;
  const perLen = numbers.length;
  for (let i = 0; i < perLen; i++) {
    const arr = [...new Array(perLen - i).fill("+"), ...new Array(i).fill("-")];
    const permus = generateUniquePermutations(arr);
    permus.forEach((p) => {
      const res = calc(p, numbers);
      if (res == target) {
        result += 1;
      }
    });
  }
  return result;
}

solution([1, 1, 1, 1, 1], 3);
