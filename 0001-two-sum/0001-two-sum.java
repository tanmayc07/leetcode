class Solution {
    public int[] twoSum(int[] nums, int target) {
        var hm = new HashMap<Integer, Integer>();

        for (int i=0; i<nums.length; i++) {
            if (hm.containsKey(target-nums[i])) {
                return new int[]{i, hm.get(target-nums[i])};
            }
            hm.put(nums[i], i);
        }

        return new int[]{0, 0};
    }
}