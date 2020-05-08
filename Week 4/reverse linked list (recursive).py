# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ###recursive2
        if not head or not head.next:
            return head
        newhead=self.reverseList(head.next)
        head.next.next=head
        head.next=None
        return newhead
        
        
        ###recursive
        if not head:
            return head
        if head.next == None or head==None:
            return head
        
        rev =self.reverseList(head.next)
        head.next.next = head
        head.next=None
        return rev
       
        