class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        totalSum=0
        nums.sort()

        for i in range(0, len(nums), 2):
            totalSum+=nums[i]
        
        return totalSum