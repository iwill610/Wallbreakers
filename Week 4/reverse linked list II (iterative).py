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
       
        ###iterative
        justincase=ListNode(0)
        justincase.next=head
        before = justincase
        
        for i in range(m-1):
            before=before.next
        
        start=before.next
        then = start.next
        
        for i in range(n-m):
            start.next=then.next
            then.next=before.next
            before.next=then
            then=start.next
            

        return justincase.next