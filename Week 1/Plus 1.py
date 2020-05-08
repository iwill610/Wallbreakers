class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        z=[str(i) for i in digits]
        x=""
        for j in z:
            x+=j
        y=int(x)
        y=y+1
        ans = [int(l) for l in str(y)]
        return ans