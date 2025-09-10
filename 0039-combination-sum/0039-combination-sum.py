class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer=[]
        length=len(candidates)

        def dfs(start=0, stack=[], total=0):
            if total==target:
                answer.append(stack[:])
                return
            elif total>target:
                return
            for i in range(start, length):
                stack.append(candidates[i])
                dfs(i, stack, total+candidates[i])
                stack.pop()
        dfs()    
        return answer