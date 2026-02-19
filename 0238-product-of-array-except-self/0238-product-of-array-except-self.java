class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        ArrayList<Integer> pre = new ArrayList<>(Collections.nCopies(n, 0));
        ArrayList<Integer> suf = new ArrayList<>(Collections.nCopies(n, 0));

        pre.set(0, 1);
        suf.set(nums.length-1, 1);
        for (int i=1; i<nums.length; i++) {
            pre.set(i, pre.get(i-1) * nums[i-1]);
        }

        for (int j=nums.length-2; j>-1; j--) {
            suf.set(j, suf.get(j+1) * nums[j+1]);
        }

        int[] res = new int[n];
        for (int k=0; k<nums.length; k++) {
            res[k] = pre.get(k)*suf.get(k);
        }

        return res;
    }
}