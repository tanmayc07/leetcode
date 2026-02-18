class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashMap<Integer, Integer> hm = new HashMap<>();

        for (int num: nums) {
            hm.merge(num, 1, Integer::sum);
        }

        for (int val: hm.values()) {
            if(val > 1) return true;
        }

        return false;
    }
}