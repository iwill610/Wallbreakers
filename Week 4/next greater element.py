class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack=[]
        for x in nums1:
            if x in nums2: 
                stack.append(self.search(nums2,nums2.index(x)))
                
            else:
                stack.append(-1)
        return stack
    def search(self,nums2,i):
        if i!=len(nums2)-1:
            for j in nums2[i+1:]:
                if j>nums2[i]:
                    return j
        return -1