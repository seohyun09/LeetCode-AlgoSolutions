class Solution {
    public void sortColors(int[] nums) {
        int i = 0;
        int j = 0;
        int k = nums.length;

        while (j < k) {
            if(nums[j] == 0) {
                int temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
                i++;
                j++;
            } else if (nums[j] == 1) {
                j++;
            } else if (nums[j] == 2) {
                k--;
                int temp = nums[j];
                nums[j] = nums[k];
                nums[k] = temp;
            }
        }
    }
}