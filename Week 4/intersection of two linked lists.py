# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # listA = [4,1,8,4,5] listB = [5,0,1,8,4,5]
        # listB = [5,0,1,8,4,5] listA = [4,1,8,4,5]
        #ab
        #ba
        if not headA or not headB:
            return None
        
        a=headA
        b=headB
        
        while a!=b:
            #if reach end start b
            if not a:
                a=headB
            #walk through
            else: 
                a=a.next
            if not b:
                b=headA
            else: 
                b=b.next
        return a