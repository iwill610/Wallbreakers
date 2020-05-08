# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        #1
        odd = head
        #2
        even = head.next
        #attach even to back of odd
        evenhead = head.next
        while even and even.next:
            #connect odds
            odd.next=even.next
            #continue iteration
            odd=odd.next
            
            #connect evens
            even.next=odd.next
            #continue iteration
            even=even.next
        odd.next=evenhead
        return head