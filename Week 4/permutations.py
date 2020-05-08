class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans=[[]]
        for i in range(len((nums))):
            newperm=[]
            for j in range(i+1):
                for prev in ans:
                    newperm.append(prev[:j]+[nums[i]]+prev[j:])
            ans=newperm
        return ans