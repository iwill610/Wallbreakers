# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import heapq
        heap=[]
        for ll in lists:
            while ll:
                heapq.heappush(heap,ll.val)
                ll=ll.next
        
        newll=ListNode(0)
        while heap:            
            x=heapq.heappop(heap)
            x=ListNode(x)
            last=newll
            while last.next:
                last=last.next
            last.next = x
            
        return newll.next