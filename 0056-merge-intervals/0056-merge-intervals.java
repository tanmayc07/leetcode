class Solution {
    public int[][] merge(int[][] intervals) {
        if (intervals.length <= 1) return intervals;

        int[] last_merged;
        List<int[]> res = new ArrayList<>();

        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));

        last_merged = intervals[0];
        for (int i=1; i<intervals.length; i++) {
            int r1 = last_merged[1];
            int l2 = intervals[i][0];

            if (r1 >= l2) {
                last_merged[1] = Math.max(r1, intervals[i][1]);
            } else {
                res.add(last_merged);
                last_merged = intervals[i];
            }
        }

        res.add(last_merged);

        return res.toArray(new int[res.size()][]);
    }
}