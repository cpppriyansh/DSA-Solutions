class Solution:
    def reverseVowels(self, s: str) -> str:
        word = list(s)
        l = 0
        r = len(s) - 1
        vowels = "aeiouAEIOU"
    
        while l < r:
            while l < r and vowels.find(word[l]) == -1:
                l = l+1
            while l < r and vowels.find(word[r]) == -1:
                r = r-1

            word[l], word[r] = word[r], word[l]
            l += 1
            r -= 1

        return "".join(word)
