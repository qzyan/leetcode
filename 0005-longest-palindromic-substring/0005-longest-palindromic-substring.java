class Solution {
    public String longestPalindrome(String s) {
        if (s == null || s.length() == 0) {
            return "";
        }
        
        Boolean[][] is_pals = new Boolean[s.length()][s.length()];
        for (int row_idx = 0; row_idx < s.length(); row_idx++) {
            for (int col_idx = 0; col_idx < s.length(); col_idx++) {
                is_pals[row_idx][col_idx] = false;
            }
        }
        
        for (int idx = 0; idx < s.length(); idx++) {
            is_pals[idx][idx] = true;
        }
        
        for (int idx = 1; idx < s.length(); idx++) {
            is_pals[idx][idx - 1] = true;
        }
        
        int start_idx = 0;
        int max_len = 1;
        
        for (int len = 2; len < s.length() + 1; len++) {
            for (int row_idx = 0; row_idx < s.length() - len + 1; row_idx++) {
                int col_idx = row_idx + len - 1;
                is_pals[row_idx][col_idx] = is_pals[row_idx + 1][col_idx - 1] && s.charAt(row_idx) == s.charAt(col_idx);
                
                if (is_pals[row_idx][col_idx]) {
                    max_len = len;
                    start_idx = row_idx;
                }
            }
        }
        
        return s.substring(start_idx, start_idx + max_len);
    }
}