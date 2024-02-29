// 숫자들과 3가지의 연산문자(+, -, *)
const splitString = (str) => {
  let temp = "";
  const operSet = new Set();
  const numArr = [];

  for (let i = 0; i < str.length; i++) {
    if (isNaN(str[i])) {
      numArr.push(Number(temp));
      numArr.push(str[i]);
      operSet.add(str[i]);
      temp = "";
    } else {
      temp = temp + str[i];
    }
  }
  numArr.push(Number(temp));
  return [operSet, numArr];
};

const permutations = (array, num) => {
  if (num == 1) return array.map((item) => [item]);
  const result = [];
  array.forEach((fixed, i, o) => {
    const extra = [...o.slice(0, i), ...o.slice(i + 1)];
    const attached = permutations(extra, num - 1);
    result.push(...attached.map((com) => [fixed, ...com]));
  });
  return result;
};

const getPermutation = (sets = new Set()) => {
  const arr = [...sets];
  return permutations(arr, arr.length);
};

const calcul = (a, b, op) => {
  switch (op) {
    case "*":
      return a * b;
    case "+":
      return a + b;
    case "-":
      return a - b;
  }
};

const getScore = (numArr = [], progressArr) => {
  let numArrCopy = [...numArr];
  let cnt = 0;
  let queue = [];
  let operque = [];

  while (!(numArrCopy.length == 1 && !operque.length && !queue.length)) {
    if (numArrCopy.length == 0) {
      numArrCopy = [...queue];
      queue = [];
      cnt++;
      continue;
    }
    const char = numArrCopy.shift();
    if (!isNaN(char)) {
      if (operque.length >= 2) {
        operque.push(char);
        const [a, op, b] = operque;
        const v = calcul(a, b, op);
        queue.push(v);
        operque = [];
        continue;
      }
      queue.push(char);
      continue;
    }
    const currentOper = progressArr[cnt];

    if (char == "+") {
      if (currentOper == "+") {
        operque.push(queue.pop());
        operque.push(char);
        continue;
      }
      queue.push(char);
      continue;
    }
    if (char == "-") {
      if (currentOper == "-") {
        operque.push(queue.pop());
        operque.push(char);
        continue;
      }
      queue.push(char);
      continue;
    }
    if (char == "*") {
      if (currentOper == "*") {
        operque.push(queue.pop());
        operque.push(char);
        continue;
      }
      queue.push(char);
      continue;
    }
  }
  return Math.abs(numArrCopy[0]);
};

function solution(expression) {
  const [operSet, numArr] = splitString(expression);
  const operCombinations = getPermutation(operSet);
  let answer = 0;
  operCombinations.forEach((v) => {
    answer = Math.max(answer, getScore(numArr, v));
  });
  return answer;
}

console.log(solution("100-200*300-500+20"));
