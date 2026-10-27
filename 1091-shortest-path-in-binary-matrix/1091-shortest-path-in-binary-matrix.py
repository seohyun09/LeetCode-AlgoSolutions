from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:

        INF = float('inf')
        
        n = len(grid)
        m = len(grid[0])

        # 상, 하, 좌, 우, 좌상, 우상, 좌하, 우하
        di = [-1, 1, 0, 0, -1, -1, 1, 1]
        dj = [0, 0, -1, 1, -1 ,1, -1, 1]

        visited = [[-1] * m for _ in range(n)]

        def bfs(si, sj):
            nonlocal visited

            que = deque()
            que.append([si, sj])
            
            visited[si][sj] = 1

            while que:
                i, j = que.popleft()
                
                for d in range(8):
                    ni = i + di[d]
                    nj = j + dj[d]

                    if ni < 0 or ni >= n or nj < 0 or nj >= m:
                        continue
                    
                    if visited[ni][nj] == -1 and grid[ni][nj] == 0:
                        visited[ni][nj] = visited[i][j] + 1
                        que.append([ni, nj])
            
        if grid[0][0] == 0:
            bfs(0, 0)

        return visited[n-1][m-1]

