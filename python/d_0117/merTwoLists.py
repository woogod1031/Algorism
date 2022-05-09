from graphlib import TopologicalSorter
from typing import Optional

#Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#            self.val = val
#            self.next =next

class Solution:
    def merTwoLists(self, l1, l2):
        # l1 = [], l2 = [] ==> []
        # li = [], l2 = [0] ==> l2
        if not l1:
            return l2

        if not l2:
            return l1

        #from <= to
        ans = None
        if l1.val <= l2.val:
            fromPoint = l1
            toPoint = l2
            ans = fromPoint
        else:
            fromPoint = l2
            toPoint = l1
            ans = fromPoint

        while fromPoint != None:
            if fromPoint.val <= toPoint.vla:
                while fromPoint.next != None and fromPoint.next.val <= toPoint.val:
                    fromPoint = fromPoint.next

                temp =fromPoint.next
                fromPoint.next = toPoint

                fromPoint = temp
            else:
                temp =fromPoint
                fromPoint, toPoint = toPoint, temp

        return ans


                                
        


     


