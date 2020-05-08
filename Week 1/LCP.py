class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        #ans = ""
        if len(strs)==0:
            return ""
        x = min(strs,key=len)
        strs.remove(x)
        for i in range(len(strs)): #i=word
            ans = ""
            if len(x)==0:
                break
            for j in range(len(strs[i])): #j=letter
                if j<len(x) and x[j]==strs[i][j]:
                    ans+=x[j]
                else:
                    break
            x=ans
        return x