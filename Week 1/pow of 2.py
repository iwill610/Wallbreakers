class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        z=[]
        for i in range(50):
            x=2**i
            z.append(x)
        if n in z:
            return True
        else:
            return False