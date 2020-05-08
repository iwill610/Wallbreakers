class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid)==0:
            return 0
        isl=0
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j]=='1':
                    self.search(grid,row,col,i,j)
                    isl+=1

        return isl
    def search(self,grid,row,col,x,y):
        if grid[x][y]=='0':
            return 
        grid[x][y]='0'
        if x!=0:
            self.search(grid,row,col,x-1,y)
        if x!=row-1:
            self.search(grid,row,col,x+1,y)
        if y!=0:
            self.search(grid,row,col,x,y-1)
        if y!=col-1:
            self.search(grid,row,col,x,y+1)  