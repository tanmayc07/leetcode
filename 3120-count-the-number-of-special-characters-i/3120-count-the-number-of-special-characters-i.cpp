class Solution {
public:
    int numberOfSpecialChars(string word) {
        unordered_set<int> st;
        for (char c: word) st.insert(c);
        int cnt = 0;
        for (char c: st) if (islower(c) && st.contains(toupper(c))) cnt += 1;
        return cnt;
    }
};