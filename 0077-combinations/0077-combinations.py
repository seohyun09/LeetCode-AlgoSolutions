class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        stack=[]
        answer=[]

        def dfs(num=0):
            if len(stack)==k:
                answer.append(stack[:])
                return
            for i in range(num+1, n+1):
                stack.append(i)
                dfs(i)
                stack.pop()
            
        dfs()
        return answer
