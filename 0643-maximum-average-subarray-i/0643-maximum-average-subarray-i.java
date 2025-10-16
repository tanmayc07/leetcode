class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int i=0, j=0, s=0, ms=Integer.MIN_VALUE;
        while(j<nums.length) {
            s+=nums[j];
            if(j-i+1==k) {
                ms = Math.max(s, ms);
                s-=nums[i];
                i++;
            }
            j++;
        }
        return (double)ms/k;
    }
}