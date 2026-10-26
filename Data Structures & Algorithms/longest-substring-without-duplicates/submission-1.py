class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = set()
        l = 0
        max_length = 0
        for i in range(len(s)):
            while s[i] in used:
                used.remove(s[l])
                l += 1
            
            W = i - l + 1
            max_length = max(max_length, W)
            used.add(s[i])
        return max_length