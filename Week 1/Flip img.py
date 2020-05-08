class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        # for i in range(len(A)):
        #     A[i]=reversed(A[i])
        for row in range(len(A)):
            for col in range(len(A[row])):
                if A[row][col]==0:
                    A[row][col]=1
                else:
                    A[row][col]=0
        for i in range(len(A)):
            A[i]=reversed(A[i])     
        return A