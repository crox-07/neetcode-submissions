class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_s = {}
        letter_t = {}
        for letter in s:
            if letter in letter_s:
                letter_s[letter] += 1
            else:
                letter_s[letter] = 1
        for letter in t:
            if letter in letter_t:
                letter_t[letter] += 1
            else: 
                letter_t[letter] = 1
        if len(letter_s) != len(letter_t):
            return False
        for key, value in letter_s.items():
            if key not in letter_t or letter_t[key] != value:
                return False
        return True
        