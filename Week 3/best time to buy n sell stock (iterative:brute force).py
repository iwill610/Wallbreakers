class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        
        if len(prices)<2:
            return 0
        minp=prices[0]
        maxp=prices[0]
        answer=[]
        for i in prices:
            if i>maxp:
                maxp=i
                
            if i<minp:
                minp=i
                maxp=i
            answer.append(maxp-minp)   
        return max(answer)