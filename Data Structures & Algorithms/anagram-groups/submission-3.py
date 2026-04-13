
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
        return False

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        seen = set()
        for i, s in enumerate(strs):
            if s in seen:
                continue
            group = [s]
            for j in range(i + 1, len(strs)):
                s2 = strs[j]
                if self.isAnagram(s, s2):
                    group.append(s2)
                    seen.add(s2)
            output.append(group)
            seen.add(s)
        return output