class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram = {}
        count = 0
        for char in s:
            if char in anagram:
                anagram[char] += 1
            else:
                anagram[char] = 1
        for char in t:
            if char in anagram:
                anagram[char] -= 1
                count += 1
                if anagram[char] < 0:
                    return False
            else:
                return False
        if len(s) == count:
            return True
        # if all(v == 0 for v in anagram.values()):
        #     return True
        return False

            