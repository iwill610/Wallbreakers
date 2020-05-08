class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        import collections
        S=collections.Counter(s)
        P=collections.Counter(p)
        
        ans=[]
        if len(s)<len(p):
            return ans
        if len(s)==len(p) and S==P:
            return [0]
        if len(P)==1 and len(p)>1:
            for i in range(len(s)):
                if s[i] in p:
                    ans.append(i)
                    break
            return ans
        for let in range(len(s)):
            if s[let] in p:
                self.ana(s,p,let,P,ans)
            else:
                continue
                
        return ans       
                
    def ana(self,s,p,let,P,ans):
        words =''
        
        for i in range(let,len(s)):
            if s[i] in p:
                words+=s[i]
                if len(words)==len(p):
                    break
                else:
                    continue
            else:
                return
        w=collections.Counter(words)
        if len(words)!= len(p):
            return
        for i in words:
            if w[i]==P[i]:
                continue
            else:
                return
        ans.append(let)
        return