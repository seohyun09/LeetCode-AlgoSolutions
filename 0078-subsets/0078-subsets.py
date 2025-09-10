class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        stack=[]
        answer=[]
        max_length=len(nums)
        visited=[False]*22

        def dfs(j=0):
            answer.append(stack[:])
            if len(stack)==max_length or len(stack)>0 and stack[-1]==nums[-1]:
                return
            for i in range(j, max_length):
                if visited[nums[i]]: continue
                stack.append(nums[i])
                visited[nums[i]]=True
                dfs(i)
                stack.pop()
                visited[nums[i]]=False
            
        dfs()
        return answer
