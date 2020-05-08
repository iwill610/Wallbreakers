class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        import collections
        S = collections.Counter(s)
        T = collections.Counter(t)
        
        for i in t:
            if S[i]!=T[i]:
                return i