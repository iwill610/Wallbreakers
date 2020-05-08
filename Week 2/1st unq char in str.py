class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        import collections
    
        S = collections.Counter(s)
        for i in range(len(s)):
            if S[s[i]]==1:
                return i
        return -1