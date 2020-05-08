###recursion dfs and backtracking
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans=[]
        #start with base case
        self.dfs(ans,0,[],nums)
        return ans
   
    def dfs(self,ans,idx,path,nums):
        ans.append(path)
        for i in range(idx,len(nums)):
            self.dfs(ans,i+1,path+[nums[i]],nums)