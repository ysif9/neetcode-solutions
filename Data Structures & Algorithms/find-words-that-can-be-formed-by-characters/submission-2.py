from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counter = Counter(chars)
        i = 0
        for word in words:
            w_counter = Counter(word)
            w_len = 0
            for w in w_counter:
                ccounter = counter.copy()
                while w_counter[w] > 0:
                    if w in ccounter and ccounter[w] > 0:
                        print(w)
                        ccounter[w] -= 1
                        w_counter[w] -= 1
                        w_len += 1
                    else: break
            if w_len == len(word):
                i += len(word)
        return i