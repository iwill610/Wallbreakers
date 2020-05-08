class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        count=0
        z=x^y
        while z>0:
            count+=z&1
            z=z>>1
        return count