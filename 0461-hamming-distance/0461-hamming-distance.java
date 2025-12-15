class Solution {
    public int hammingDistance(int x, int y) {
        int result = x ^ y;
        String bin = Integer.toBinaryString(result);
        int answer = 0;

        for (int i = 0; i < bin.length(); i++) {
            if (bin.charAt(i) == '1') answer++;
        }
        return answer;
    }
}