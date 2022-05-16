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

    this.현재노드 = undefined;
    this.데이터수 = 0;
  }

  length() {
    return this.데이터수;
  }

  append(data) {
    let node = new Node(data);

    if (this.head === null) {
      this.head = node;
      this.tail = node;
    } else {
      this.tail.next = node;
      node.prev = this.tail;
      this.tail = node;
    }

    this.length++;
  }

  toString() {
    let 순회용현재노드 = this.head;
    순회용현재노드 = 순회용현재노드.next;

    let s = "";
    for (let i = 0; i < this.데이터수; i++) {
      s += `${순회용현재노드.data},`;
      순회용현재노드 = 순회용현재노드.next;
    }
    return `[${s.slice(0, -2)}]`;
  }

  get fullData() {
    let 순회용현재노드 = this.head;
    순회용현재노드 = 순회용현재노드.next;

    let s = "";
    for (let i = 0; i < this.데이터수; i++) {
      s += `${순회용현재노드.data},`;
      순회용현재노드 = 순회용현재노드.next;
    }
    return JSON.parse(`[${s.slice(0, -2)}]`);
  }

  insert(data, position = 0) {
    if (position < 0 || position > this.length) {
      return false;
    }

    let node = new Node(value);
    let current = this.head;
    let index = 0;
    let prev; // 이전 노드 값 저장

    if (position === 0) {
      if (this.head === null) {
        this.head = node;
        this.tail = node;
      } else {
        node.next = current;
        current.prev = node;
        this.head = node;
      }
    } else if (position === this.length) {
      current = this.tail;
      current.next = node;
      node.prev = current;
      this.tail = node;
    } else {
      while (index++ < position) {
        prev = current;
        current = current.next;
      }
      node.next = current;
      prev.next = node;

      current.prev = node;
      node.prev = prev;
    }
    this.length++;

    return true;
  }
}
