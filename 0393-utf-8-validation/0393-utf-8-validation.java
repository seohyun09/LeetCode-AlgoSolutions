class Solution {
    public boolean validUtf8(int[] data) {
        for (int i = 0; i < data.length; i++) {
            if ((data[i] >= 0b11000000) && (data[i] <= 0b11011111)) {
                if (validate(data, i + 1, 1) == true) {
                    i += 1;
                    continue;
                } else return false;
            } else if ((data[i] >= 0b11100000) && (data[i] <= 0b11101111)) {
                if (validate(data, i + 1, 2) == true) {
                    i += 2;
                    continue;
                } else return false;
            } else if ((data[i] >= 0b11110000) && (data[i] <= 0b11110111)) {
                if (validate(data, i + 1, 3) == true) {
                    i += 3;
                    continue;
                } else return false;
            } else if ((data[i] >= 0b00000000) && (data[i] <= 0b01111111)) {
                if (data.length - 1 == i) return true;
            } else return false;
        }
        return true;
    }
    private boolean validate(int[] data, int idx, int time) {
        for (int i = idx; i < idx + time; i++) {
            if (i < data.length && (data[i] >= 0b10000000) && (data[i] <= 0b10111111)) continue;
            else return false;
        }
        return true;
    }
}