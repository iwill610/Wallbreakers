class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        st = str.split()
        pat={}
        s={}
        if len(pattern)!=len(st):
            return False
        for i,let in enumerate(pattern):
            pat[let]=pat.get(let,[])+[i]
        for j,w in enumerate(st):
            s[w]=s.get(w,[])+[j]
        for w in range(len(st)):
            if s[st[w]]!=pat[pattern[w]]:
                return False
        return True