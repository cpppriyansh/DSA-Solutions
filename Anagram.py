class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        result = {}
        result1 = {}
        for i in range(len(s)):
            key = s[i] 
            if key not in result:
                result[key] = 1
            else:
                result[key] += 1
        
        for i in range(len(t)):
            key = t[i]
            if key not in result1:
                result1[key] = 1
            else:
                result1[key] += 1

        return result == result1
            
