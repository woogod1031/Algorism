class Node:
    def __init__(self,item,next):
        self.item = item
        self.next = next

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        self.top =Node(value,self.top)

    def pop(self):
        if self.top is None:
            return None

        '''
        Node(5, node 4) <- Top
        Node(4, node 3)
        Node(3, node 2)
        Node(2, node 1)
        Node(1, node None)
        '''
        topNode = self.top
        self.top = self.top.next
        return topNode.item

    def is_empty(self):
        return self.top is None
        #True, False    