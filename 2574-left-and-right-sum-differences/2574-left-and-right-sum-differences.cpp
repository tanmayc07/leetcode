class Solution {
public:
    vector<int> leftRightDifference(vector<int>& nums) {
        vector<int> pre(nums.size(), 0);
        vector<int> res;

        int ts = accumulate(nums.begin(), nums.end(), 0);
        res.push_back(abs(0-(ts-nums[0])));
        ts -= nums[0];

        for (int i=1; i<nums.size(); i++) {
            pre[i] = nums[i-1]+pre[i-1];
            res.push_back(abs(pre[i]-(ts-nums[i])));
            ts -= nums[i];
        }    
        
        return res;
    }
};