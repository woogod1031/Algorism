import Node from "./LinkedNode";

//Linked List는 배열과 달리 메모리상에 index에 의한 물리적 배치를 하지 않고
//node를 생성 후 해당 node의 pointer에 의해 다음 node를 연결
//이를 통해 Linked List는 데이터 삽입/삭제시 데이터의 구조를 재정렬하지 않아도 된다.

class LinkedList {
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

    this.tail.next = newNode;
    this.tail = newNode;
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
    let currentNode = this.head;
    currentNode = currentNode.next;

    for (let i = 0; i < index - 1; i++) {
      currentNode = currentNode.next;
    }

    let newNode = new Node(data);

    newNode.next = currentNode.next;
    currentNode.next = newNode;

    this.dataNum += 1;
  }
}

l = new LinkedList();

l.append(1);
l.append(2);
l.append(3);
l.insert(2, 5);
console.log(l.length());
console.log(l.toString());
