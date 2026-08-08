class Solution {
    public int smallestNumber(int n, int t) {
        for (int i=n; i<=n+10; i++) {
            int pr = 1;
            int cp = i;
            while (cp!=0) {
                int d = cp%10;
                pr = pr*d;
                cp = cp/10;
            }
            if (pr%t == 0) {
                return i;
            }
        }

        return -1;
    }
}