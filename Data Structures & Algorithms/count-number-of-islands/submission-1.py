class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands=0
        ROWS,COLUMNS=len(grid),len(grid[0])
        directions=[[0,1], [0,-1], [1,0], [-1,0]]

        def bfs(r,c):
            q=deque()
            grid[r][c]='0'
            q.append((r,c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (nr<0 or nc<0 or nr>=ROWS or nc>=COLUMNS or grid[nr][nc]=='0'):
                        continue
                    q.append((nr,nc)) # add the element that was 1
                    grid[nr][nc]='0' # mark it visited



        for r in range(ROWS):
            for c in range(COLUMNS):
                if grid[r][c]=='1':
                    islands=islands+1
                    bfs(r,c)
        return islands