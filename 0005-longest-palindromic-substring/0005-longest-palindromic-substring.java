class Solution {
    public class Pair {
        public int start_idx;
        public int length;
        
        public Pair(int start_idx, int length) {
            this.start_idx = start_idx;
            this.length = length;
        }
    }

    public String longestPalindrome(String s) {
        if (s == null || s.length() == 0) {
            return "";
        }
        
        int max_len = 0;
        int start_idx = -1;
        for (int i = 0; i < 2 * s.length() - 1; i++) {
            int left, right;
            if (i % 2 == 0) {
                left = i / 2;
                right = i / 2;
            } else {
                left = i / 2;
                right = i / 2 + 1;
            }
            
            Pair answer = find_longest(s, left, right);
            
            if (answer.length > max_len) {
                max_len = answer.length;
                start_idx = answer.start_idx;
            }
        }
        
        return s.substring(start_idx, start_idx + max_len);
    }
    
    public Pair find_longest(String s, int left, int right) {
        if (s.charAt(left) != s.charAt(right)) {
            return new Pair(-1, -1);
        }
        
        while (left >= 0 && right < s.length()) {
            if (s.charAt(left) != s.charAt(right)) {
                break;
            }
            
            left -= 1;
            right += 1;
        }
        
        return new Pair(left + 1, right - left - 1);
    }
}