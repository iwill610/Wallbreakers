class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans=[]
        
        def dfs(num,comb):
            if len(comb)==k:
                ans.append(comb)
                return
            for i in range(num,n+1):
                dfs(i+1,comb+[i])
        
        dfs(1,[])
        return ans