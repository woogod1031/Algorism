function solution(citations = []) {
  citations.sort((a, b) => b - a); // 65310

  for (let i = 0; i < citations.length; i++) {
    if (citations[i] >= i + 1) continue;
    return i;
  }
  return citations.length;
}

// h인덱스는 여러개인데 그 중에서 가장 큰 거
// 예를들어 1번 이상 인용된 논문 => 4, 1편 이상
// 예를들어 2번 이상 인용된 논문 => 3, 2편 이상
// 예를들어 3번 이상 인용된 논문 => 3, 3편 이상
// 예를들어 4번 이상 인용된 논문 => 2, 4편 미만

// 즉 h인덱스는 1,2,3 중에서 가장 큰 3이 되는 거다.

// if (citations[i] >= i + 1) continue;
// return i;

// 이 코드는 만약 내림차순으로 되어 있는 citations에서 citations[i]값이 i+1번 이상 인용된 논문 보다 작다는 건
// i+1편 미만이므로 이전 편수를 통해 최대 h인덱스를 반환할 수 있다.
