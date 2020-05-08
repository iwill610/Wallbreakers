class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        return set(nums1) & set(nums2)
       
    
    ###Attempt 1 **works**
        # c = set(nums1+nums2)
        # return [i for i in c if (i in nums1 and i in nums2)]