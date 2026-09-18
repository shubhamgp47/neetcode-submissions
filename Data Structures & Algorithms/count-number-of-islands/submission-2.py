class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # same as 1
        distance=[[0,1], [0,-1], [1,0], [-1,0]]
        ROWS, COLUMNS = len(grid),len(grid[0])
        count = 0

        def dfs(r,c):
            grid[r][c]=0 #make the element already visited 0
            for dr,dc in distance:
                nr,nc = r+dr, c+dc
                if nc<0 or nr <0 or nr>=ROWS or nc>=COLUMNS:
                    continue
                if grid[nr][nc]=="1":
                    dfs(nr,nc)
        
        for r in range(ROWS):
            for c in range(COLUMNS):
                if grid[r][c]=="1":
                    count=count+1
                    dfs(r,c)
        return count

