class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''solve using dfs - find a 1 and for that 1 try finding the longest chain of 1's associated to that 1 and make them 0.'''
        distance = [[0,1], [0,-1], [1,0], [-1,0]]
        islands=0
        ROWS,COLUMNS=len(grid),len(grid[0])

        def dfs(r,c):
            if(r<0 or r>=ROWS or c<0 or c>=COLUMNS or grid[r][c]=="0"):
                return
            grid[r][c]="0"
            for dr, cr in distance:
                dfs(r+dr, c+cr)

        for r in range(ROWS):
            for c in range(COLUMNS):
                if grid[r][c]=="1":
                    islands=islands+1
                    dfs(r,c)
        return islands
        