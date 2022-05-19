import Node from "./StackNode";

class Queue {
  constructor() {
    this.head = null;
    this.tail = null;
    this.length = 0;
  }
  enqueue(data) {
    let newNode = new Node(data);
    if (this.length == 0) {
      this.head = newNode;
    } else {
      this.tail.next = newNode;
    }
    this.tail = newNode;
    this.length++;
  }
  dequeue() {
    if (this.length == 0) {
      return null;
    }
    let currentNode = this.head.data;
    this.head = this.head.next;
    this.length--;
    if (this.length == 0) {
      this.tail = null;
    }
    return currentNode;
  }
  isEmpty() {
    return this.length == 0;
  }
}
