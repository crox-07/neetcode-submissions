class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        l = 0
        max_length = 0
        for i in range(len(s)):
            while s[i] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[i])
            W = (i - l) + 1
            if W > max_length:
                max_length = W
                
        return max_length


