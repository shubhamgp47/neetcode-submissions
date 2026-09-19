class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        distance =[[0,1],[0,-1],[1,0],[-1,0]]
        time=0
        ROWS,COLUMNS=len(grid),len(grid[0])
        fresh=0

        for r in range(ROWS):
            for c in range(COLUMNS):
                if grid[r][c]==2:
                    q.append((r,c))
                if grid[r][c]==1:
                    fresh=fresh+1
                    
        while q and fresh > 0:
            qLen=len(q)
            for i in range(qLen):
                r,c = q.popleft()
                for dr, dc in distance:
                    nr, nc = r+dr, c+dc
                    if nr<0 or nc<0 or nr>=ROWS or nc>=COLUMNS or grid[nr][nc]==0:
                        continue
                    if grid[nr][nc]==1:
                        grid[nr][nc]=2
                        fresh=fresh-1
                        q.append((nr,nc))
            time=time+1
        if fresh==0:
            return time
        else:
            return -1
                