class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lenS1 = len(s1)
        count = [0] * 26
        
        for i in range(lenS1):
            count[ord(s1[i]) - ord('a')] += 1
        
        R = lenS1 - 1
        L = 0
        while R < len(s2):
            countS2 = [0] * 26
            for i in range(L, R + 1, 1):
                countS2[ord(s2[i]) - ord('a')] += 1
            matches = 0
            for i in range(26):
                matches += 1 if count[i] == countS2[i] else 0
            print(matches)
            if matches == 26:
                return True
            L += 1
            R += 1
        return False