class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[1 for _ in range(len(nums))]
        front_product=1
        back_product=1

        for i in range(len(nums)):
            result[i]*=front_product
            front_product*=nums[i]
        
        for i in range(len(nums)-1, -1, -1):
            result[i]*=back_product
            back_product*=nums[i]

        return result