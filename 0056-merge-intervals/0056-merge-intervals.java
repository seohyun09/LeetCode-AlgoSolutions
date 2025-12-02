class Solution {
    public int[][] merge(int[][] intervals) {
        if (intervals.length == 1) return intervals;

        List<List<Integer>> list = new ArrayList<>();
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
        list.add(new ArrayList<>(Arrays.asList(intervals[0][0], intervals[0][1])));

        for (int i = 1; i < intervals.length; i++) {
            int first = list.get(list.size() - 1).get(0);
            int second = list.get(list.size() - 1).get(1);

            if (first <= intervals[i][0] && intervals[i][0] <= second) {
                if (intervals[i][1] > second) {
                    list.get(list.size() - 1).set(1, intervals[i][1]);
                }
            } else {
                list.add(new ArrayList<>(Arrays.asList(intervals[i][0], intervals[i][1])));
            }
        }

        int[][] result = new int[list.size()][2];
        for (int i = 0; i < list.size(); i++) {
            result[i][0] = list.get(i).get(0);
            result[i][1] = list.get(i).get(1);
        }
        return result;
    }
}