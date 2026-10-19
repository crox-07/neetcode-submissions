from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_collections = defaultdict(list)
        outputs = []

        def add_to_collections(letters: tuple, word: str) -> None:
            if letters in str_collections:
                str_collections[letters].append(word)
            else: str_collections[letters] = [word]

        for word in strs:
            letters = [0] * 26
            if len(word) == 0:
                add_to_collections(tuple(letters), word)
                continue
            for l in word:
                index = ord(l) - ord("a")
                letters[index] += 1
            letters = tuple(letters)
            add_to_collections(letters, word)
        return [group for group in str_collections.values()]

        #     letters = {}
        #     for l in word:
        #         if l in letters:
        #             letters[l] += 1
        #         else: letters[l] = 1
        #     im_letters = (letters)
        #     if im_letters in str_collections.keys():
        #         str_collections[(letters)].append(word)
        #     else: str_collections[(letters)] = [word]
        # outputs = [x for x in str_collections.values()]
        # return outputs

            # for i in range(len(str_collections)):
            #     if letters == str_collections[i]:
            #         if type(output[i]) == list:
            #             output[i] += word
            #         else: 
            #             output.append(word)
            #     else
            
