import Node from "./LinkedNode";

//Linked List는 배열과 달리 메모리상에 index에 의한 물리적 배치를 하지 않고
//node를 생성 후 해당 node의 pointer에 의해 다음 node를 연결
//이를 통해 Linked List는 데이터 삽입/삭제시 데이터의 구조를 재정렬하지 않아도 된다.

class LinkedList {
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
    let 새로운노드 = new Node(data);

    this.tail.next = 새로운노드;
    this.tail = 새로운노드;
    this.데이터수 += 1;
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

  insert(index, data) {
    let 순회용현재노드 = this.head;
    순회용현재노드 = 순회용현재노드.next;

    for (let i = 0; i < index - 1; i++) {
      순회용현재노드 = 순회용현재노드.next;
    }

    let 새로운노드 = new Node(data);

    새로운노드.next = 순회용현재노드.next;
    순회용현재노드.next = 새로운노드;

    this.데이터수 += 1;
  }
}

l = new LinkedList();

l.append(1);
l.append(2);
l.append(3);
l.insert(2, 5);
console.log(l.length());
console.log(l.toString());
