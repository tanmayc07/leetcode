class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> map = new HashMap<>();

        for (int i=0; i<s.length(); i++) {
            map.merge(s.charAt(i), 1, Integer::sum);
        }

        for (int i=0; i<t.length(); i++) {
            if (map.containsKey(t.charAt(i))) {
                map.put(t.charAt(i), map.get(t.charAt(i))-1);
            } else {
                return false;
            }
        }

        if (map.size() == 0) {
            return false;
        }

        return true;
    }
}