// 소수 판별에서 어려웠음
function isPrime(num) {
  if (num === 0) return false;
  if (num === 1) return false;

  for (let i = 2; i < Math.sqrt(num + 1); i++) {
    if (num % i === 0) return false;
  }
  return true;
}

function solution(numbers) {
  numbers = numbers.split("");
  const length = numbers.length;
  let set = new Set();

  function getCombination(array, index, result) {
    set.add(Number(result.join("")));
    if (result.length == length) {
      return;
    }
    const newArray = [...array.slice(0, index), ...array.slice(index + 1)];
    for (let i = 0; i < newArray.length; i++) {
      getCombination(newArray, i, [...result, newArray[i]]);
    }
  }

  for (let i = 0; i < numbers.length; i++) {
    getCombination(numbers.slice(), i, [numbers[i]]);
  }
  const array = new Array(...set);

  return array.filter((v) => {
    return isPrime(v);
  }).length;
}

// console.log(isPrime(1231));
console.log(solution("1231"));
