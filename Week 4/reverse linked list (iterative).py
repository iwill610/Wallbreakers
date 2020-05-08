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
       
        
        ###iterative
        rev = None
        while head:
            holdtherest=head.next
            #print(hold)
            head.next = rev
            #print(head.next)
            rev = head
            #print(rev)
            head = holdtherest
            #print(head)
        return rev