class Solution {
    public String largestNumber(int[] nums) {
        if (Arrays.stream(nums).sum() == 0) return "0";

        int i = 0;
        while (i < nums.length) {
            int j = i;
            while (j > 0) {
                String first = String.valueOf(nums[j-1]);
                String second = String.valueOf(nums[j]);
                if ((second + first).compareTo(first + second) > 0) {
                    int temp = nums[j];
                    nums[j] = nums[j - 1];
                    nums[j - 1] = temp;
                    j--;
                } else {
                    break;
                }
            }
            i++;
        }
        StringBuilder answer = new StringBuilder();
        for (int num : nums) {
            answer.append(num);
        }
        return answer.toString();
    }
}