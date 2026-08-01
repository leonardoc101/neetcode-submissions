class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()){
            return false;
        }
        char[] s_list = s.toCharArray();
        char[] t_list = t.toCharArray();
        Arrays.sort(s_list);
        Arrays.sort(t_list);
        return Arrays.equals(s_list, t_list);
    }
}
