class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> hm = new HashMap<>();

        for(int i=0; i<strs.length; i++) {
            char[] temp = strs[i].toCharArray();
            Arrays.sort(temp);
            String sorted_str = new String(temp);

            hm.computeIfAbsent(sorted_str, k -> new ArrayList<String>()).add(strs[i]);
        }

        return new ArrayList<>(hm.values());
    }
}