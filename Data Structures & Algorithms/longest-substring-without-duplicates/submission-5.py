class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: 
            return 0
        seen = set()
        left = 0
        a = 0
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[i])
            if i - left + 1 > a:
                a = i - left + 1
        return a  