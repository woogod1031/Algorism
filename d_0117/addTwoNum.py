from typing import List
import collections

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(self, l1,l2):
    node, prev = l1, None
    while node:
       next, node.next = node.next, prev
       node,prev = next, node
    
    node2, prev2 = l2, None
    while node2:
       next2, node2.next = node2.next, prev2
       node2, prev2 = next2, node2
    
    def addlist(self,node):
        list = []
        while node:
            list.append(node.val)
            node = node.next
        return list
    
    list1 = addlist(prev)
    list2 = addlist(prev2)
    resultStr = int(''.join(str(c) for c in list1)) + int(''.join(str(c) for c in list2))
    def torevered(self, result):
        prev = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node
        
        return node
    return torevered(str(resultStr))


list1 = ListNode(1)
list2 = ListNode(2)
list3 = ListNode(2)
list4 = ListNode(1)
list1.next = list2
list2.next = list3
list3.next = list4
head = list1
        
print(reverseList(head))
        

    