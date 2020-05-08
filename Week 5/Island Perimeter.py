class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        
        def P(x,y,grid,p):
            if  x < 0 or y < 0 or x==len(grid) or y==len(grid[0]) or grid[x][y]==0:
                return p+1
            elif grid[x][y]=='visited':
                return p
            grid[x][y]='visited'
            p = P(x+1,y,grid,p)            
            p = P(x-1,y,grid,p)     
            p = P(x,y+1,grid,p) 
            p = P(x,y-1,grid,p) 
            return p
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col]==1:
                    print(row)
                    print(col)
                    return P(row,col,grid,0)