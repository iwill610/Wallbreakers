# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        ###recursive
        if m==n:
            return head
        if m>1:
            newhead=head
            newhead.next=self.reverseBetween(head.next,m-1,n-1)
            return newhead
        if m==1:
            newhead=self.reverseBetween(head.next,m,n-1)
            xx=head.next.next
            head.next.next=head
            head.next=xx
            return newhead
        
