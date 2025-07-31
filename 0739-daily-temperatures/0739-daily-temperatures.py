class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        result=[0]*len(temperatures)

        for i in range(len(temperatures)):
            j=i
            while stack and stack[-1][0]<temperatures[i]:
                num, idx=stack.pop()
                result[idx]=i-idx
                if not stack: break
            stack.append([temperatures[i], i])
        
        return result
                