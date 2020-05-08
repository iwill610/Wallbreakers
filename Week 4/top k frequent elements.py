import collections
import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ### heaps and collections counter
        c = collections.Counter(nums)
        heap=[]
        
        for num in c:
            heapq.heappush(heap,(c[num],num))
            if len(heap)>k:
                heapq.heappop(heap)
        return [x[1] for x in heap]
       
        
        ###collections counter most common solution
        return [x[0] for x in collections.Counter(nums).most_common(k)]