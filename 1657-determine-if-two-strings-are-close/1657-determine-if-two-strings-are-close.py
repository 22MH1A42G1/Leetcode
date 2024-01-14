class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        a = set(word1)==set(word2) 
        b = sorted(Counter(word1).values())
        c = sorted(Counter(word2).values())
        d = (b==c)
        return a and d