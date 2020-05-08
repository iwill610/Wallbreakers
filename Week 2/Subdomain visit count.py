class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        import collections
        ans = collections.Counter()
        for dom in cpdomains:
            count,dom=dom.split()
            count = int(count)
            indom=dom.split('.')
            for idom in range(len(indom)):
                ans['.'.join(indom[idom:])]+=count
        x=[]
        y=''
        for i in ans:
            
            y = str(ans[i])+" "+str(i)
            x.append(y)
            y=''
        return x