class Solution {
    public int search(int[] nums, int target) {
        if (nums.length == 1 && nums[0] == target) return 0;

        int k = 0;
        if (nums[0] == target) return 0;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i - 1] > nums[i]) {
                k = i;
                break;
            }
            if (nums[i] == target) {
                return i;
            }
        }
        
        if (target < nums[k]) {
            return -1;
        }

        // binary serach
        int start = k;
        int end = nums.length - 1;
        int mid = (start + end) / 2;

        while (start <= end) {
            if (target < nums[mid]) {
                end = mid - 1;
            } else if (target > nums[mid]) {
                start = mid + 1;
            } else if (nums[mid] == target) {
                return mid;
            }
            mid = (start + end) / 2;
        }
        return -1;
    }
}