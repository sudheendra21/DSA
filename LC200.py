class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        r = len(grid)
        c = len(grid[0])

        num = 0
        

        def dfs(i,j):

            if i < 0 or i > r-1 or j < 0 or j > c-1 :
                return 
            if grid[i][j] == '0':
                return
            
            grid[i][j] = '0'

            dir = [(-1,0),(1,0),(0,1),(0,-1)]

            for dx,dy in dir :
                
                dfs(i+dx,j+dy)
            



        
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1':

                    dfs(i,j)
                    num = num+1
        
        return num
        


        
        