from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        fresh=0
        q=deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    fresh+=1
                elif grid[i][j]==2:
                    q.append((i,j))
        minutes=0
        while q and fresh>0:
            size=len(q)
            for i in range(size):
                i,j=q.popleft()
                if i-1>=0 and grid[i-1][j]==1:
                    grid[i-1][j]=2
                    q.append((i-1,j))
                    fresh-=1

                if  i+1<n and grid[i+1][j]==1:
                    grid[i+1][j]=2
                    q.append((i+1,j))
                    fresh-=1

                if  j-1>=0 and grid[i][j-1]==1:
                    grid[i][j-1]=2
                    q.append((i,j-1))
                    fresh-=1

                if  j+1<m and grid[i][j+1]==1:
                    grid[i][j+1]=2
                    q.append((i,j+1))
                    fresh-=1
            minutes+=1  
        if fresh==0:
            return minutes
        return -1