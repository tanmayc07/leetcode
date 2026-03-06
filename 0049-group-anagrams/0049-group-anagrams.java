class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> hm = new HashMap<>();

        for (String st: strs) {
            char[] charr = st.toCharArray();
            Arrays.sort(charr);
            String sortedKey = new String(charr);

            if (!hm.containsKey(sortedKey)) {
                hm.put(sortedKey, new ArrayList<>());
            }
            hm.get(sortedKey).add(st);
        }

        return new ArrayList<>(hm.values());
    }
}