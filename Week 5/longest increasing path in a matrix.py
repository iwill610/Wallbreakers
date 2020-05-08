class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def path(row,col,current,count):
            if store[row][col] != -1:
                return store[row][col]
            ans = 1
            for directions in LRupdown:
                x, y = row + directions[0], col + directions[1]
                if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]) or matrix[x][y] <= current:
                    continue
                count = 1 + path(x,y,matrix[x][y],count)
                ans = max(count,ans)
            store[row][col]=ans    
            return store[row][col]


        ans = 0
        store = [[-1] * len(matrix[0]) for row in range(len(matrix))]
        LRupdown = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        if not matrix or not matrix[0]:
            return 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                paths = path(i,j,matrix[i][j],0)
                ans = max(ans,paths)
             
        
        return ans