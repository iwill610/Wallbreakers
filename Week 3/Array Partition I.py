class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        ans = 0
        for ai in range(len(nums)):
            if ai%2==0:
                ans+=nums[ai]
        return ans   