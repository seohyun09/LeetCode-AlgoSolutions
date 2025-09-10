class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        stack=[]
        answer=[]

        def dfs(j=0):
            if sum(stack)==target:
                answer.append(stack[:])
                return
            elif sum(stack)>target:
                return
            for i in range(j, len(candidates)):
                stack.append(candidates[i])
                dfs(i)
                stack.pop()
        dfs()
        
        return answer