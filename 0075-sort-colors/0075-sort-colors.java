class Solution {
    public void sortColors(int[] nums) {
        if (nums.length == 2 && nums[0] <= nums[1]) {
            return;
        }
        for (int i = 0; i < nums.length - 1; i++) {
            int num = nums[i + 1];
            int idx = i + 1;
            for (int j = i + 1; j < nums.length; j++) {
                if (num > nums[j]) {
                    num = nums[j];
                    idx = j;
                }
            }
            if (nums[i] > num) {
                int temp = nums[i];
                nums[i] = num;
                nums[idx] = temp;
            }
        }
    }
}