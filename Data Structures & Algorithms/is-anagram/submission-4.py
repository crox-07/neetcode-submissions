class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_s, letter_t = {}, {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            letter_s[s[i]] = 1 + letter_s.get(s[i], 0)
            letter_t[t[i]] = 1 + letter_t.get(t[i], 0)
        for key in letter_s:
            if letter_t.get(key, 0) != letter_s[key]:
                return False
        return True


        # for letter in s:
        #     if letter in letter_s:
        #         letter_s[letter] += 1
        #     else:
        #         letter_s[letter] = 1
        # for letter in t:
        #     if letter in letter_t:
        #         letter_t[letter] += 1
        #     else: 
        #         letter_t[letter] = 1
        # if len(letter_s) != len(letter_t):
        #     return False
        # for key, value in letter_s.items():
        #     if key not in letter_t or letter_t[key] != value:
        #         return False
        # return True
        