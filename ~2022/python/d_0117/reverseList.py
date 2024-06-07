# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node, prev = head, None

        while node:
           next, node.next = node.next, prev
           node,prev = next, node
    
        return prev       


class Solution(object):
    def reverseList(self, head):
        def reverse(node,prev:None):
            if not node:
                return prev
            next, node.next = node.next,prev
            return reverse(next,node)

        return reverse(head)

        