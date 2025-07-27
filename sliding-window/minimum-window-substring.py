class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        t_count = Counter(t)
        s_count = defaultdict(int)
        included_char_count = 0
        left, right = 0, 0
        min_len = float("inf")
        result_l, result_r = 0, 0
        while right < len(s):
            char = s[right]
            right += 1
            # not related
            if char not in t_count:
                continue

            s_count[char] += 1
            if s_count[char] == t_count[char]:
                included_char_count += 1

            if included_char_count < len(t_count):
                continue

            while left < right:
                left_char = s[left]
                if left_char not in t_count:
                    left += 1
                    continue
                                
                if right - left < min_len:
                    min_len = right - left
                    result_l = left
                    result_r = right
                
                if s_count[left_char] == t_count[left_char]:
                    break

                s_count[left_char] -= 1
                left += 1
        
        return s[result_l: result_r] if min_len != float("inf") else ""
                
                


