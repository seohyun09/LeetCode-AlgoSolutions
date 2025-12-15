class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        for (int i = 0; i < matrix.length; i++) {
            if (matrix[i][0] > target) return false;

            if (binarySearch(matrix[i], target) == true) {
                return true;
            }
        }
        return false;
    }
    private boolean binarySearch(int[] row, int target) {
        int start = 0;
        int end = row.length - 1;
        int mid;

        while (start <= end) {
            mid = (start + end) / 2;
            if (row[mid] == target) return true;
            else if (row[mid] < target) {
                start = mid + 1;
            } else if (row[mid] > target) {
                end = mid - 1;
            }
        }
        return false;
    }
}