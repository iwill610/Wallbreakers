class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        import collections
        S = collections.Counter(s)
        ans=''
        for letter,i in S.most_common(len(S)):
            ans+= letter*i
        return ans