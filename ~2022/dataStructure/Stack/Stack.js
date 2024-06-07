import Node from "./StackNode";

//노드 출력(정/역방향)
//노드 추가
//특정 인덱스 노드 추가
//노드 삭제
//특정 인덱스 노드 삭제
//특정 노드 인덱스 출력

class Stack {
  constructor() {
    let init = new Node("init");
    this.head = init; //처음에 데이터가 없다면 head는 null이다.
    this.tail = init;
    this.length = 0;
  }

  length() {
    return this.length;
  }
  peek() {
    // stack에 쌓인 가장 마지막 녀석을 확인하는 메소드
    return this.head;
  }

  push(data) {
    let newNode = new Node(data);

    if (this.length === 0) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      let currentNode = this.head;
      this.head = newNode;
      this.head.next = currentNode;
    }
    this.length++;
  }
  pop() {
    if (!this.head) null;
    else if (this.head === this.tail) {
      this.tail = null;
    } else {
      this.head = this.head.next;
      this.length--;
      return this;
    }
  }
}
