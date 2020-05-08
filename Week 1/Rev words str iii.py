class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans=" "
        z=s.split()
        for i in range(len(z)):
            z[i]=z[i][::-1]
        return ans.join(z)