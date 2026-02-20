class Solution {
    public int subarraySum(int[] nums, int k) {
        int res = 0;
        HashMap<Integer, Integer> hm = new HashMap<>();
        hm.put(0, 1);

        int ps = 0;
        for(int num: nums) {
            ps += num;
            if(hm.containsKey(ps - k)) {
                res += hm.get(ps-k);
            }
            hm.put(ps, hm.getOrDefault(ps, 0) + 1);
        }

        return res; 
    }
}