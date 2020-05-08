class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vow ="aeiouAEIOU"
        A=[str(i) for i in s]
        rev = [0]*len(A)
        j=0
        for i in range(len(A)):
            if A[i] in vow:
                rev[j]=A[i]
                j+=1
        for i in range(len(A)):
            if A[i] in vow:
                j-=1
                A[i]=rev[j]
                      
        return ''.join(A)