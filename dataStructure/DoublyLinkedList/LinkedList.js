import Node from "./LinkedNode";

//노드 출력(정/역방향)
//노드 추가
//특정 인덱스 노드 추가
//노드 삭제
//특정 인덱스 노드 삭제
//특정 노드 인덱스 출력

class DoubleyLinkedList {
  constructor() {
    let init = new Node("init");
    this.head = init; //처음에 데이터가 없다면 head는 null이다.
    this.tail = init;
    this.dataNum = 0;
  }

  length() {
    return this.dataNum;
  }

  append(data) {
    let newNode = new Node(data);

    if (this.head.data === "init") {
      this.head = newNode;
      this.tail = newNode;
    } else {
      this.tail.next = newNode;
      newNode.prev = this.tail;
      this.tail = newNode;
    }
    this.dataNum += 1;
  }

  get fullData() {
    let currentNode = this.head;
    currentNode = currentNode.next;

    let s = "";
    for (let i = 0; i < this.dataNum; i++) {
      s += `${currentNode.data},`;
      currentNode = currentNode.next;
    }
    return JSON.parse(`[${s.slice(0, -1)}]`);
  }

  insert(index, data) {
    let currentNode = this.head; //순회용
    let newNode = new Node(data);

    if (index === 0) {
      newNode.next = currentNode;
      if (currentNode != null) {
        currentNode.prev = newNode;
      }
      this.head = newNode;
    } else if (index === this.dataNum) {
      let tailNode = this.tail;
      tailNode.next = newNode;
      newNode.prev = tailNode;
      this.tail = newNode;
    } else {
      for (i = 0; i < index - 1; i++) {
        currentNode = currentNode.next;
      }
      newNode.next = currentNode.next;
      currentNode.next.prev = newNode;

      currentNode.next = newNode;
      newNode.prev = currentNode;
    }

    this.dataNum += 1;
  }

  remove(index) {
    const currentNode = this.head;
    if (index === 0) {
      this.head = this.head.next;
      if (head != null) {
        this.head.prev = null;
      }
    } else if (index === this.dataNum) {
      this.tail = this.tail.prev;
      this.tail.next = null;
    } else {
      for (let i = 0; i < index - 1; i++) {
        currentNode = currentNode.next;
      }
      const deleteNode = currentNode.next;
      const afterNode = deleteNode.next;
      currentNode.next = afterNode;
      afterNode.prev = currentNode;
    }
  }
}
