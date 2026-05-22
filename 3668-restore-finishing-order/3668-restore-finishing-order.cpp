class Solution {
public:
    vector<int> recoverOrder(vector<int>& order, vector<int>& friends) {
        unordered_set<int> s;
        for (auto it: friends) s.insert(it);
        vector<int> ans;
        for (auto it: order)
            if (s.contains(it)) ans.push_back(it);
        return ans;
    }
};