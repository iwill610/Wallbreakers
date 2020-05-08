class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        jewels=set()
        for i in J:
            jewels.add(i)
        for j in S:
            if j in jewels:
                count+=1
        return count