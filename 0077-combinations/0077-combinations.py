class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        stack=[]
        visited=[False]*22
        answer=[]

        def dfs(num=1):
            if len(stack)==k:
                answer.append(stack[:])
                return
            elif len(stack)>0 and stack[-1]==n:
                return
            for i in range(num, n+1):
                if visited[i]: continue
                elif len(stack)>0 and stack[-1]>i: continue
                stack.append(i)
                visited[i]=True
                dfs(num+1)
                stack.pop()
                visited[i]=False

        dfs()
        return answer