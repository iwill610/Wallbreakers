class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        si = {}
        ti = {}
        for i,let in enumerate(s):
            si[let]=si.get(let,[])+[i]
        for j,let in enumerate(t):
            ti[let]=ti.get(let,[])+[j]
        return sorted(si.values())==sorted(ti.values())