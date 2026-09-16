class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=deque()
        time=0
        fresh=0
        distance = [[1,0], [-1,0], [0,1], [0,-1]]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==2:
                    q.append((r,c))
                elif grid[r][c]==1:
                    fresh=fresh+1
        
        while q and fresh>0:
            length=len(q)
            for i in range(length):
                r,c = q.popleft()

                for dr, dc in distance:
                    nr, nc = r+dr, c+dc
                    if nr in range(len(grid)) and nc in range(len(grid[0])) and grid[nr][nc]==1:
                        grid[nr][nc]=2
                        fresh=fresh-1
                        q.append((nr,nc))
            time=time+1
        if fresh==0:
            return time
        else:
            return -1