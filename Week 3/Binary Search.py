class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lb,ub = 0,len(nums)-1
        while lb<=ub:
            move = lb+(ub-lb)//2
            if nums[move]==target:
                return move
            if target<nums[move]:
                ub=move-1
            else:
                lb=move+1
        return -1
        
        
        ###either works 
        
        
        for i in range(len(nums)):
            if nums[i]==target:
                return i
        return -1