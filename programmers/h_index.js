function solution(citations = []) {
  citations.sort((a, b) => b - a); // 0 1 3 5 6

  const startValue = citations[0];

  const totalArray = new Array(
    citations[0] - citations[citations.length - 1] + 1
  )
    .fill(0)
    .map((_, index) => {
      return startValue - index;
    });

  for (let i = 0; i < totalArray.length; i++) {
    const h = totalArray[i];
    const refferLength = citations.filter((v) => {
      if (v >= h) return true;
      return false;
    }).length;

    const restLength = citations.length - refferLength;

    if (refferLength >= h && restLength <= h) return h;
  }

  return citations.length;
}

console.log(solution([9, 9, 9, 9, 1]));
//
