class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        #hw3 sorting
        answer=[]
        inp = set(p)
        for letter in range(len(s)-len(p)+1):
            if s[letter] in inp:
                if self.check(s[letter:len(p)+letter],p):
                    answer.append(letter)
            else:
                continue
        return answer
    def check(self,x,p):
        hi=list(x)
        hello=list(p)
        hi.sort()
        hello.sort()
        return hi==hello