class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            others=nums[i+1:]
            for j in range(len(others)):
                if (nums[i]+others[j])==target:
                    return i, j+i+1