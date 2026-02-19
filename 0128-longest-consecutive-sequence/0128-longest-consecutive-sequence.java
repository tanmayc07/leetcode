class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        int largest = 0;
        Set<Integer> numsSet = new HashSet<>();
        for (int num: nums) numsSet.add(num);

        for (int num: numsSet) {
            if (!numsSet.contains(num-1)) {
                int curr = num;
                while (numsSet.contains(curr)) {
                    curr += 1;
                }
                largest = Math.max(largest, curr-num);
            }
        }

        return largest;
    }
}