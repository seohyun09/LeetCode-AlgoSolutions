class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        stack=[]
        visited=[False]*22
        answer=[]

        def dfs():
            if len(stack)==len(nums):
                answer.append(stack[:])
                return
            for i in range(len(nums)):
                if visited[nums[i]]==True:
                    continue
                stack.append(nums[i])
                visited[nums[i]]=True
                dfs()
                stack.pop()
                visited[nums[i]]=False
        
        dfs()
        return answer