class Solution {
    public int firstUniqChar(String s) {
        int c = -1;
        for (int i=0; i<s.length(); i++) {
            int f = 0;
            for (int j=0; j<s.length(); j++) {
                if (i != j && s.charAt(i) == s.charAt(j)) {
                    f = 1;
                    break;
                }
            }
            if (f == 0) {
                c = i;
                break;
            }
        }

        return c;
    }
}