class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited=[[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        dx=[1, -1, 0, 0] # 좌우
        dy=[0, 0, 1, -1] # 상하
        numOfIsland=0

        def dfs(x, y):
            visited[x][y]=True
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if nx>=0 and nx<len(grid) and ny>=0 and ny<len(grid[0]) and grid[nx][ny]=="1" and visited[nx][ny]==False:
                    dfs(nx, ny)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1" and visited[i][j]==False:
                    numOfIsland+=1  
                    dfs(i, j)                  

        return numOfIsland