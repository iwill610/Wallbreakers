class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        cycle = set()
    
        ans = n
        
        while ans != 1:
            n=str(ans)
            add=0
            x = [int(i) for i in n ]
            for dig in range(len(x)):
                add+=x[dig]**2
            ans=add
            if ans not in cycle:
                cycle.add(ans)
                if ans == 1:
                    return 1==ans
            else:
                break
        return 1==ans