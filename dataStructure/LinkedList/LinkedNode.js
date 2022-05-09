export default class Node {
  constructor(data) {
    //data와 next를 넣고 next의 디폴트는 null로 지정 왜냐하면 linkedlist의 tail(마지막은) null로 끝나기때문
    this.data = data;
    this.next = null;
  }
}
