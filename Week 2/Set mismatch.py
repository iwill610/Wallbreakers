class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        import collections 
        N = collections.Counter(nums)
        ans=[]
        correct=[i for i in range(1,len(nums)+1)]
        
        for num,i in N.most_common(1):
            ans.append(num)
            break
        for i in correct:
            if i not in nums:
                ans.append(i)
                break
        return ans