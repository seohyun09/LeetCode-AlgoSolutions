class Solution {
    public int getSum(int a, int b) {
        while (b != 0) {
            int xor = a ^ b;
            int and = a & b;
            int carry = and << 1;
            a = xor;
            b = carry;
        }
        return a;
    }
} 