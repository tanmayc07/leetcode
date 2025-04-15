class Solution {
    public int lengthOfLongestSubstring(String s) {
        int i=0, j=0, ml=-1;
        HashMap<Character, Integer> mp = new HashMap<>();

        while(j<s.length()) {
            mp.put(s.charAt(j), mp.getOrDefault(s.charAt(j), 0) + 1);

            if(mp.size() == j-i+1) {
                ml = Math.max(ml, j-i+1);
            } else if(mp.size() < j-i+1) {
                while(mp.size() < j-i+1) {
                    mp.put(s.charAt(i), mp.get(s.charAt(i))-1);
                    if(mp.get(s.charAt(i)) == 0) {
                        mp.remove(s.charAt(i));
                    }
                    i++;
                }
            }
            j++;
        }
        if(ml>0) return ml;
        else return 0;
    }
}