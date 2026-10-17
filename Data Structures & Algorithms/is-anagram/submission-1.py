class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters_s = {}
        letters_t = {}
        for char in s:
            if char in letters_s:
                letters_s[char] += 1
            else: letters_s[char] = 1
        for char in t:
            if char in letters_t:
                letters_t[char] += 1
            else: letters_t[char] = 1

        if len(letters_s) != len(letters_t):
            return False
        for key, value in letters_s.items():
            if letters_t.get(key) != value:
                return False
        return True
        