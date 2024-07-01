function h_push(array, value) {
  array.push(value);
  let currentIndex = array.length - 1;

  while (
    currentIndex > 0 &&
    array[currentIndex] < array[Math.floor((currentIndex - 1) / 2)]
  ) {
    let parrentIndex = Math.floor((currentIndex - 1) / 2);
    [array[currentIndex], array[parrentIndex]] = [
      array[parrentIndex],
      array[currentIndex],
    ];
    currentIndex = parrentIndex;
  }
}

function h_pop(array) {
  if (array.length === 0) return null;
  if (array.length === 1) return array.pop();

  // 값 제거
  const minValue = array[0];
  array[0] = array.pop();

  // 하향 이동 (down-heapify)
  let currentIndex = 0;
  while (currentIndex * 2 + 1 < array.length) {
    let leftChildIndex = currentIndex * 2 + 1;
    let rightChildIndex = currentIndex * 2 + 2;

    let minChildIndex =
      rightChildIndex < array.length &&
      array[rightChildIndex] < array[leftChildIndex]
        ? rightChildIndex
        : leftChildIndex;

    if (array[currentIndex] < array[minChildIndex]) {
      break;
    }

    [array[currentIndex], array[minChildIndex]] = [
      array[minChildIndex],
      array[currentIndex],
    ];
    currentIndex = minChildIndex;
  }

  return minValue;
}

function solution(scoville, K) {
  const minHeap = [];

  for (const sco of scoville) {
    h_push(minHeap, sco);
  }

  let mixedCount = 0;

  while (minHeap.length > 1 && minHeap[0] < K) {
    const [first, second] = [h_pop(minHeap), h_pop(minHeap)];
    h_push(minHeap, first + second * 2);
    mixedCount += 1;
  }

  if (minHeap.length == 1) {
    if (minHeap[0] >= K) return mixedCount;
    return -1;
  }
  return mixedCount;
}

// class MinHeap {
//   constructor() {
//     this.heap = [];
//   }

//   size() {
//     return this.heap.length;
//   }

//   // 값을 넣되, 오름차 순 정렬함
//   push(value) {
//     this.heap.push(value);
//     let currentIndex = this.heap.length - 1;

//     while (
//       currentIndex > 0 &&
//       this.heap[currentIndex] < this.heap[Math.floor((currentIndex - 1) / 2)]
//     ) {
//       let parrentIndex = Math.floor((currentIndex - 1) / 2);
//       const temp = this.heap[currentIndex];
//       this.heap[currentIndex] = this.heap[parrentIndex];
//       this.heap[parrentIndex] = temp;
//       currentIndex = parrentIndex;
//     }
//   }

//   // 값을 빼되, 오름차 순 정렬 함
//   pop() {
//     if (this.heap.length === 0) return null;
//     if (this.heap.length === 1) return this.heap.pop();

//     // 값 제거
//     const minValue = this.heap[0];
//     this.heap[0] = this.heap.pop();

//     // 하향 이동 (down-heapify)
//     let currentIndex = 0;
//     while (currentIndex * 2 + 1 < this.heap.length) {
//       let leftChildIndex = currentIndex * 2 + 1;
//       let rightChildIndex = currentIndex * 2 + 2;

//       let minChildIndex =
//         rightChildIndex < this.heap.length &&
//         this.heap[rightChildIndex] < this.heap[leftChildIndex]
//           ? rightChildIndex
//           : leftChildIndex;

//       if (this.heap[currentIndex] < this.heap[minChildIndex]) {
//         break;
//       }

//       [this.heap[currentIndex], this.heap[minChildIndex]] = [
//         this.heap[minChildIndex],
//         this.heap[currentIndex],
//       ];
//       currentIndex = minChildIndex;
//     }

//     return minValue;
//   }

//   peek() {
//     return this.heap[0];
//   }
// }

// function solution(scoville, K) {
//   const minHeap = new MinHeap();

//   for (const sco of scoville) {
//     minHeap.push(sco);
//   }
//   scoville.sort((a, b) => b - a);

//   let mixedCount = 0;

//   while (minHeap.size() > 1 && minHeap.peek() < K) {
//     const [first, second] = [minHeap.pop(), minHeap.pop()];
//     minHeap.push(first + second * 2);
//     mixedCount += 1;
//   }

//   if (minHeap.size() == 1) {
//     if (minHeap.peek() >= K) return mixedCount;
//     return -1;
//   }
//   return mixedCount;
// }

// console.log(solution([1, 2, 3, 9, 10, 12], 7));

// // 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
