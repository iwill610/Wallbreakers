class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sc=0
        tc=0
        if len(s)!=len(t):
            return False
        else:
            for i in s:
                if i in t:
                    sc+=ord(i)
                    continue
                else:
                    return False
            for j in t:
                tc+=ord(j)
            return sc==tc