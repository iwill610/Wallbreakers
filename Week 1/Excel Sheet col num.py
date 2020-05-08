class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        diff = ord('A')-1
        if len(s) == 1:
            return ord(s)-diff
        elif len(s)>1:
            ans=0
            for i in range(len(s)-1,-1,-1):
                ans=ans+(ord(s[i])-diff)*26**((len(s)-1)-i)            
            return ans  