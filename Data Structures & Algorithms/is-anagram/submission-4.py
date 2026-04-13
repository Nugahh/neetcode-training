class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram = {}
        for char in s:
            if char in anagram:
                anagram[char] += 1
            else:
                anagram[char] = 1
        for char in t:
            if char in anagram:
                anagram[char] -= 1
            else:
                return False
        if all(v == 0 for v in anagram.values()):
            return True
        return False

            